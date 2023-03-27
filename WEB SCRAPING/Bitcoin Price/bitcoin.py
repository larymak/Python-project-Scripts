import requests
import sys


""" Exit program if no command-line argument is provided """
if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")


""" 
Convert command-line argument to float or
Exit if command line argument is not a number
"""
try:
    bitcoin = sys.argv[1]
    bitcoin = float(bitcoin)
except ValueError:
    sys.exit("Command-line argument is not a number")


"""Get Bitcoin price"""
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    rate = response.json()["bpi"]["USD"]["rate_float"]
    print(f"Current Price: ${bitcoin * rate:,.4f}")
except requests.RequestException:
    print("An Error Occurred")
