def main():
    text=input("Input: ")
    print(short(text))

def short(word):
    shorter=""

    for i in word:
        if i.lower() in ["a","e","i","o","u"]:
            continue

        shorter += i

    return shorter

if __name__ == "__main__":
    main()
