def main():
    while True:
        try:
            x,y = input("Please input value: ").split("/")
            x = int(x)
            y = int(y) 

            if x<0 or y<=0 or x>y:
                continue

            fuel = calculate(x,y)

        except(ValueError, ZeroDivisionError):
            print("Please Enter again. ")
        else:
            break

    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")

def calculate(a,b):
    return round (a / b * 100) 
    
main()
    