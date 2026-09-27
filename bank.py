#In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
def main():
    greet=input("What? ").lower().strip()
    print(greeting(greet))

def greeting(to):
    if to.startswith("hello"):
        return "$0"
    elif to.startswith("h"):
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()
