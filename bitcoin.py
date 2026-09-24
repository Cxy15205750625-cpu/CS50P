import sys
import requests

def main():
    n = argument()

    try:
        response = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=a294f476b338d357f2a00af6a27e322bf06664498bb7320ec5fdeeba492e9b10"
    )
    except requests.RequestException:
        sys.exit("Network wrong. ")

    data = response.json()
    price = float(data["data"]["priceUsd"])
    total = n * price

    print(f"${total:,.4f}")

def argument():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number. ")

main()
