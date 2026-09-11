def main():
    camel_name()

def camel_name():
    result = ""
    camel_case = input("Please enter camel case: ")

    for char in camel_case:
        if char.isupper():
            result += "_" + char.lower()

        else:
            result += char

    print("snake_case: ", result)



main()
