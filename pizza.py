import sys
from tabulate import tabulate
import csv

def main():
    check_length()
    check_extension()
    try:
        with open(sys.argv[1]) as file:
            rows = csv.reader(file)
            header = next(rows)
            data = list(rows)

            print(tabulate(data, headers=header, tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("The file is not exist. ")

def check_length():
    if len(sys.argv) != 2:
        sys.exit("Wrong argument length. ")

def check_extension():
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Wrong extension. ")


main()
