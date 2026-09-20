import inflect

def main():
    p = inflect.engine()

    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            break

    print(p.join(names))

main()
