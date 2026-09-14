def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            True
        else:
            return False

        text = False
        for char in s:
            if char.isdigit():
                    text=True
            else:
                return False

        if not s.isalnum():
                return False


main()
