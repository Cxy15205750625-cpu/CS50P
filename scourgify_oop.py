import sys
import csv

class Student:
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
                    #把 class Student 生成的数据存到 student 里，方便我们可以用
                    student = Student(first, last, house)

                    #Write the changed name to new csv. With the attribute. 所以，有什么好处用class？就是稍微清爽一点，用一种更抽象的方式组织了代码，更清晰，更加能看得清楚现在在干什么，也方便以后迭代，如果要迭代，也无非就是class 里面加点参数，比如后面还要求传入学生的体检数据，只要用一样的方式写就行了。
                    writer.writerow({
                        "first": student.first_name,
                        "last": student.last_name,
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
