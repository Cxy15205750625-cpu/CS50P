from PIL import Image, ImageOps
import sys
import os

def main():
    check_length()
    check_extension()

    try:
        shirt = Image.open("shirt.png")
        photo = Image.open(sys.argv[1])
        fitted_photo = ImageOps.fit(photo, shirt.size)
        fitted_photo.paste(shirt, shirt)
        fitted_photo.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("The file does not exist. ")

def check_length():
    if len(sys.argv) != 3:
        sys.exit("Wrong command-arguments. ")

def check_extension():
    _, before_ext = os.path.splitext(sys.argv[1])
    _, after_ext = os.path.splitext(sys.argv[2])
    before_ext = before_ext.lower()
    after_ext = after_ext.lower()
    if before_ext != after_ext:
        sys.exit("The command-arguments extensions are not same. ")

    if before_ext not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Wrong command-argument extension. ")

    if after_ext not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Wrong command-argument extension. ")



if __name__ == "__main__":
     main()
