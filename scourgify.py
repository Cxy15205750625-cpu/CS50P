import sys
import csv

def main():
    check_length()
    check_extension()
    try:
        with open(sys.argv[1]) as input_file:
            reader = csv.DictReader(input_file)

            with open(sys.argv[2], "w") as output_file:
                writer = csv.DictWriter(
                    output_file,
                    fieldnames=["first", "last", "house"]
                )

                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")

                    writer.writerow({
                        "first": first,
                        "last": last,
                        "house": row["house"]
                    })

    except FileNotFoundError:
            sys.exit("The file is not exist. ")

def check_length():
    if len(sys.argv) != 3:
        sys.exit("Wrong argument length. ")

def check_extension():
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Wrong extension. ")

main()
