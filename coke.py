def main():
    machine()

def machine():
    due=50

    while due > 0 :
        print("Amount Due: ", due)
        put_in = int(input("Insert coin: "))
        
        if put_in == 25:
            due -= put_in

        elif put_in == 10:
            due -= put_in

        elif put_in == 5:
            due -= put_in

        else:
            continue

    print("change owed: ", -due)

main()
