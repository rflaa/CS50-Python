import requests
import sys

def main():
    try:
        if len(sys.argv) == 2:
            data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
            price = float(data["bpi"]["USD"]["rate_float"]) * float(sys.argv[1])
            print(f"${price:,.4f}")
        else:
            sys.exit("Missing command-line argument")

    except ValueError:
        sys.exit("Invalid argument")
    except requests.RequestException:
        sys.exit("Could not retrieve data")

main()
