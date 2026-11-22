from tools.run_python_file import run_python_file


def test() -> None:
    result = run_python_file("tools", "main.py")
    print(result)

    result = run_python_file(".", "test_get_files_info.py")
    print(result)

    result = run_python_file("tools", "tests.py")
    print(result)

    result = run_python_file("tools", "../main.py")
    print(result)

    result = run_python_file(".", ".py")
    print(result)

    result = run_python_file("testtools", "lorem.txt")
    print(result)


if __name__ == "__main__":
    test()
