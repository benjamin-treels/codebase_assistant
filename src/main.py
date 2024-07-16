
import ollama
from read_codebase import read_codebase
from langchain.docstore.document import Document
import chromadb

excluded_dirs = []
codebase_root_dir = ""
codebase = read_codebase(codebase_root_dir, excluded_dirs)

print("\033[1;32mCreating documents...\033[0m")
documents: list[Document] = []
for filepath, code in codebase.items():
    document = Document(page_content="\n".join(filepath + " : " + code), metadata={"source": filepath})
    documents.append(document)

client = chromadb.Client()
collection = client.create_collection(name="docs")

print("\033[1;34mCreating vector store...\033[0m")
for i, d in enumerate(documents):
  code = d.page_content.replace("\n", "")
  response = ollama.embeddings(model="nomic-embed-text", prompt=code)
  embedding = response["embedding"]

  collection.add(
    ids=[str(i)],
    embeddings=[embedding],
    metadatas=[d.metadata],
    documents=[code]
  )

while True:
  prompt = input("Please enter your prompt (or type 'exit' to quit): ")
  if prompt.lower() == 'exit':
      print("Exiting the loop. Goodbye!")
      break
  
  response = ollama.embeddings(
      prompt=prompt,
      model="nomic-embed-text"
  )
  
  print("\033[1;32mRetrieve document for prompt...\033[0m")
  results = collection.query(
      query_embeddings=[response["embedding"]],
  )
  
  data = ""
  for document in results["documents"][0]:
      print(document.split(":")[0]) #filename
      data += document
  
  print("\033[1;34mGenerate response...\033[0m")
  response = ollama.generate(
      model="llama3",
      prompt=f"Using this data: {data}. Respond to this prompt: {prompt}"
  )
  
  print(response["response"])



    


