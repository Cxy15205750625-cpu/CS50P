import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)"
    match = re.fullmatch(pattern, s)

    if not match:
        raise ValueError("Invalid time format. ")

    start_hour = int(match.group(1))
    start_minute = match.group(2) or "00"
    start_period = match.group(3)

    over_hour = int(match.group(4))
    over_minute = match.group(5) or "00"
    over_period = match.group(6)

    start_hour %= 12
    over_hour %= 12

    if start_period == "PM":
        start_hour += 12

    if over_period == "PM":
        over_hour += 12

    return f"{start_hour:02d}:{start_minute} to {over_hour:02d}:{over_minute}"

if __name__ == "__main__":
    main()
