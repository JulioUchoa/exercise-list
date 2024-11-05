import sys
import requests

btc = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
obj = btc.json()
btc_price = obj['bpi']['USD']['rate_float']


try:
    nv = btc_price * float(sys.argv[1])
    print("${:,.4f}".format(nv))


except (requests.RequestException, ValueError):
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit()
    if not int(sys.argv[1]):
        print("Command-line argument is not a number")
        sys.exit()

