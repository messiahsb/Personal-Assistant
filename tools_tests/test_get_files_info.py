from tools.get_files_info import get_files_info


def test() -> None:
    result = get_files_info("testtools", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("testtools", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("testtools", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("testtools", "../")
    print("Result for '../' directory:")
    print(result)

    result = get_files_info("testtools", "test")
    print("Result for '../' directory:")
    print(result)


if __name__ == "__main__":
    test()
