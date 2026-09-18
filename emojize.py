import emoji

#先调用 emoji library, 拿取用户输入的str数据, 讨论两种情况，如果是code格式，则直接转换。如果是alias格式，还需要加上  language = ... 主要错误出在 IndexError.
while True:
    text = input("Index: ")

    try:
        print(emoji.emojize(text, language = "alias"))

    except IndexError:
        continue

    break
