def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not 2 <= len(s) <= 6:
            return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    if not s.isalnum():
        return False

    number_started=False

    for char in s:
        if char.isdigit():
            if not number_started:
                number_started = True

                if char == "0":
                    return False

        elif number_started:
            return False

    return True

main()
