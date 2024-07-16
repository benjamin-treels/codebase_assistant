import os
from src.read_codebase import read_codebase
import pytest

@pytest.fixture(autouse=True)
def setup_files():
    print("\n== Setup beforeEach ==")

    global codebase_dir
    codebase_dir = os.path.join(os.getcwd(), "codebase")
    src_dir = os.path.join(codebase_dir, "src")

    try:
        os.makedirs(src_dir)

        alice_path = os.path.join(codebase_dir, "alice.txt")
        bob_path = os.path.join(codebase_dir, "bob.txt")
        main_path = os.path.join(src_dir, "main.py")
        invalid_utf8_path = os.path.join(codebase_dir, "invalid_utf8.txt")

        alice_content = "alice content file"
        bob_content = "bob content file"
        main_content = "print('Hello World')"
        invalid_utf8_content = "éàèùçô".encode('latin-1')

        with open(alice_path, "w", encoding="utf-8") as f:
            f.write(alice_content)

        with open(bob_path, "w", encoding="utf-8") as f:
            f.write(bob_content)

        with open(main_path, "w", encoding="utf-8") as f:
            f.write(main_content)

        with open(invalid_utf8_path, "wb") as f:
            f.write(invalid_utf8_content)

        yield

    finally:
        for file_path in [alice_path, bob_path, main_path, invalid_utf8_path]:
            if os.path.exists(file_path):
                os.remove(file_path)

        if os.path.exists(src_dir):
            os.rmdir(src_dir)
        if os.path.exists(codebase_dir):
            os.rmdir(codebase_dir)


'''
should load files and their content into dict 
'''
def test_load_files_happy_flow():
    expected = {
        "alice.txt": "alice content file",
        "bob.txt": "bob content file",
        os.path.join("src", "main.py"): "print('Hello World')"
    }
    directory = os.path.join(os.getcwd(), codebase_dir)

    result = read_codebase(directory)
    print(result)

    assert result == expected

''' 
should ignore files that are not utf-8 encoded
'''
def test_load_files_with_latin1():
    expected = {
        "alice.txt": "alice content file",
        "bob.txt": "bob content file",
        os.path.join("src", "main.py"): "print('Hello World')"
    }
    directory = os.path.join(os.getcwd(), codebase_dir)

    result = read_codebase(directory)

    assert result == expected

'''
should ignore dirs within excluded_dirs
'''
def test_ignore_dirs():
    expected = {
        "alice.txt": "alice content file",
        "bob.txt": "bob content file",
    }
    directory = os.path.join(os.getcwd(), codebase_dir)

    result = read_codebase(directory, ["src"])

    assert result == expected