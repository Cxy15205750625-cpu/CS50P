def main():
    machine()

def machine():
    coin_now = 50
    print("Amount Due: ", coin_now)
    ow=0
    while coin_now > 0:
        put_in = int(input("Insert coin: "))
        print(put_in)

        if put_in == 25:
            coin_now -= put_in
        print("Change owed: ", ow)

        continue

        if put_in == 10:
            coin_now -= put_in

    while coin_now > 50:
        print("change owed: ", coin_now)
