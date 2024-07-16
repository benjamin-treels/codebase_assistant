import os

def read_codebase(directory: str, excluded_dirs: list[str] = []) -> dict[str, str]:
    '''
    Read Codebase and return each filepath with its content in dict.

    Params: directory - str : root dir of codebase
    excluded_dirs - list[str] : list of directory names to exclude
    Returns: dict[str,str] : [filepath : content, ...]
    '''
    documents = {}
    for root, dirs, files in os.walk(directory):
        # Exclude directories based on their names
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        for file in files:
            abs_path = os.path.join(root, file)
            try:
                with open(abs_path, "r", encoding="utf-8") as o:
                    content = o.readlines()
                    relative_path = os.path.relpath(abs_path, directory)
                    documents[relative_path] = ' '.join([str(elem) for elem in content])
            except UnicodeDecodeError:
                pass
    return documents