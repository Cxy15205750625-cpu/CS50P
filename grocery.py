ITEM = {}
while True:
    try:
        item = input().upper()
        if item in ITEM:
            ITEM[item] += 1
        else:
            ITEM[item] = 1

    except EOFError:
        break

    for item in sorted(ITEM):
        print(ITEM[item], item)