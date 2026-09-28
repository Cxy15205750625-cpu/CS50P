import sys

def main():
    check_length()
    check_path()
    count = 0

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.strip() == "":
                    continue

                if line.lstrip().startswith("#"):
                    continue

                count += 1

            print(count)

    except FileNotFoundError:
        sys.exit("The file is not exist. ")

def check_length():
    if len(sys.argv) != 2:
        sys.exit("Wrong argument length. ")

def check_path():
    if not sys.argv[1].endswith(".py"):
        sys.exit("Wrong extension. ")

main()
