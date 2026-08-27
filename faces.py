def main():
    text=convert(input("Enter any text"))
    print(text)

def convert(text):
    text=text.replace(":)", "🙂")
    text=text.replace(":(", "🙁")
    return text

main()
