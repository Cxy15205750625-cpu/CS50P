import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    result = re.fullmatch(
        r"([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})",
        ip
    )
    if result is None:
        return False

    if (
        0 <= int(result.group(1)) <= 255
        and 0 <= int(result.group(2)) <= 255
        and 0 <= int(result.group(3)) <= 255
        and 0 <= int(result.group(4)) <= 255
    ):
        return True

    return False

if __name__ == "__main__":
    main()
