import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font = font)
    text = input("Input: ")
    print(figlet.renderText(text))

elif len(sys.argv) == 3:
    option = sys.argv[1]
    f = sys.argv[2]

    if option in ["-f", "--font"]:
        figlet.setFont(font=f)
        text = input("Input: ")

        print(figlet.renderText(text))

    else:
        sys.exit("Wrong arguments. ")

else:
    sys.exit("Wrong number of arguments. ")

