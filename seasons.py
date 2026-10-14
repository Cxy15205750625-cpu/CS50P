#1.  获取出生日期，现在日期，得到相减值(min). 2. 将数字值改成英文输出(inflect) 3. 如果参数错误 sys.exit 退出
from datetime import date
import re
import sys
import inflect

def main():
    minutes = calculate_minutes()
    english_date = turn_english(minutes)
    print(f"{english_date} minute")

def calculate_minutes():
    try:
        user_input = input("Date of Birth: ")

        if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", user_input):
            sys.exit("Invalid date")

        year, month, day = map(int, user_input.split("-"))
        today = date.today()
        birthday = date(year, month, day)

    except ValueError:
        sys.exit("Invalid date")

    difference = today - birthday
    return difference.days * 24 * 60

def turn_english(to):
    p = inflect.engine()
    return p.number_to_words(to, andword="").capitalize()

if __name__ == "__main__":
    main()
