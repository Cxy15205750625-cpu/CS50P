def main():
    fruit=input("Item: ").lower()
    nutrition(fruit)

def nutrition(to):
    fruits = {
    "apple":130,
    "avocado":50,
    "sweet cherries":100
    }
    if to in fruits:
        print("Calories:", fruits[to])


main()
