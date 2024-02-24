import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)

try:
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = request.json()

    amount = response["bpi"]["USD"]["rate_float"] * value
    print(f"${amount:,.4f}")
except requests.RequestException:
    print("Request Exception")
