import requests
import pprint

cryptos = {
    'bitcoin': 'Qwsogvtv82FCd',
    'etherum': 'razxDUgYGNAdQ',
    'dogecoin': 'a91GCGd_u96cF',
    'shibainu': 'xz24e0BjL',
    'litecoin': 'D7B1x_ks7WhV5',
    }

crypto_input = input("enter the name of crypto:")
if crypto_input in cryptos:
    choice = cryptos[crypto_input]
else:
    print("Sorry we do not have that crypto")

url = f"https://api.coinranking.com/v2/coin/{choice}"

headers = {
    "x-access-token": "coinrankingd8901efc7e4b47aafe481b49cf5deed5d7dd3e8b27d1c6a1"
    }

r = requests.get(url, headers=headers)
response = r.json()["data"]["coin"]

pprint.pprint(response["name"])
pprint.pprint(response["symbol"])
pprint.pprint(response["price"])
