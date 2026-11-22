from tools.get_file_content import get_file_content


def test() -> None:
    result = get_file_content("testtools", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    result = get_file_content("testtools", "main.py")
    print(result)

    result = get_file_content("testtools", "test")
    print(result)

    result = get_file_content("testtools", "/bin/cat")
    print(result)

    result = get_file_content("testtools", "pkg/does_not_exist.py")
    print(result)


if __name__ == "__main__":
    test()
