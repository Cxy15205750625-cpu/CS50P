MONTHS = {
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
}

def main():
    while True:
        try:
            x,y,z = input("Date: ").split("/")
            x = int(x)
            y = int(y)

            if not z.isdigit() or not z.isalpha():
                return False

        except ValueError:
            print("please use the format that 'DD/MM/YY'! ")

        else:
            break

    print(z,f"-x:02-y:02")

main()
