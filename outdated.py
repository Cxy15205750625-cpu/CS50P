MONTHS = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def main():
    while True:
        date = input("Date: ").split()
        try:
            if "/" in date:
                x, y, z = date.split("/")
                day = int(y)
                year = int(z)

                if not x.isdigit():
                    month = MONTHS[x]
                    break
            else:
                x, y, z = date.split(" ")

                if not y.endswith(","):
                    continue
                day = int(y[:-1])
                year = int(z)

        except ValueError:
            print("please use the format that 'DD/MM/YY'! ")

    print("f{month:02}-{day:02}-{year:04}")

main()
