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
        date = input("Date: ").strip()

        try:
            if "/" in date:
                x, y, z = date.split("/")
                month = int(x)
                day = int(y)
                year = int(z)

            else:
                x, y, z = date.split()

                if not y.endswith(","):
                    continue

                month = MONTHS[x]
                day = int(y[:-1])
                year = int(z)

            if not (1 <= month <= 12 and 1 <= day <= 31 and year >= 1):
                continue

            break

        except (ValueError, KeyError):
            print("please use the format that 'MM/DD/YY'! ")
            continue

    print(f"{year:04}-{month:02}-{day:02}")

main()
