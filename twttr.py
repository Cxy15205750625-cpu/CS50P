def main():
    short()

def short():
    shorter=""
    text=input("Input: ")
    for i in text:
        if i.lower() in ["a","e","i","o","u"]:
            continue

        shorter += i

    print(shorter)


main()
