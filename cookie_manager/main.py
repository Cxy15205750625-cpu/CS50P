from jar import Jar


def main():
    jar = Jar(12)

    while True:
        print(f"\n饼干罐：{jar}")
        print(f"数量：{jar.size}/{jar.capacity}")
        action = input("1 放入，2 取出，q 退出：").strip()

        if action == "q":
            break

        if action not in ("1", "2"):
            print("请输入 1、2 或 q")
            continue

        try:
            n = int(input("多少块？"))

            if n < 0:
                print("数量不能是负数")
                continue

            if action == "1":
                jar.deposit(n)
            else:
                jar.withdraw(n)

        except ValueError:
            print("操作失败：请输入整数，并检查是否装满或不够取。")


if __name__ == "__main__":
    main()
