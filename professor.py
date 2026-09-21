import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)

        for attempt in range(3):

            try:
                answer = int(input(f"{a} + {b} = "))
            except ValueError:
                print("EEE")
            else:
                if answer == a + b:
                    score += 1
                    break
                print("EEE")

            if attempt == 2:
                print(f"{a} + {b} = {a + b}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            integer = int(input("Input: "))

            if integer not in (1, 2, 3):
                raise ValueError

        except ValueError:
            continue

        return integer

def generate_integer(level):
    if level == 1:
        level = random.randint(0, 9)

        return level

    elif level == 2:
        level = random.randint(10, 99)

        return level

    elif level == 3:
        level = random.randint(100, 999)

        return level

    else:
        raise ValueError

if __name__ == "__main__":
    main()
