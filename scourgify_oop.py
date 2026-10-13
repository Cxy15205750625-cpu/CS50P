import sys
import csv

class Name:
    def __init__(self, first_name, last_name, house):
        self.first_name = first_name
        self.last_name = last_name
        self.house = house

def main():
    #检查参数是否合法
    check_length()
    check_extension()

    try:
    #读第一个文件
        with open(sys.argv[1]) as input_file:
            #Read the csv with the method.
            reader = csv.DictReader(input_file)
            #读第二个文件
            with open(sys.argv[2], "w") as output_file:
                writer = csv.DictWriter(
                    output_file,
                    fieldnames=["first", "last", "house"]
                )

                #把first, last, house 作为表头
                writer.writeheader()

                #Iterate over the csv, and take one row at a time. And split the name. We can see them as three attributes of our class.
                for row in reader:
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    student = Name(first, last, house)

                    #Write the changed name to new csv.
                    writer.writerow({
                        "first": student.first,
                        "last": student.last,
                        "house": student.house
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
