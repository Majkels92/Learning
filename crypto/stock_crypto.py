import requests
import datetime


def downloading_data():
    global response, chosen_crypto_price, chosen_crypto_name, chosen_crypto_symbol
    cryptos = {
        'bitcoin': 'Qwsogvtv82FCd',
        'etherum': 'razxDUgYGNAdQ',
        'dogecoin': 'a91GCGd_u96cF',
        'shibainu': 'xz24e0BjL',
        'litecoin': 'D7B1x_ks7WhV5',
    }

    crypto_input = input("enter the name of crypto which You want to choose: ")
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

    chosen_crypto_symbol = response["symbol"]
    chosen_crypto_name = response["name"]
    chosen_crypto_price = response["price"]
    return response, chosen_crypto_symbol, chosen_crypto_name, chosen_crypto_price


def appending_sought_item_to_list():
    item = f"[{response_time}] {chosen_crypto_symbol}: {chosen_crypto_name} {float(chosen_crypto_price):.5f} "\
           f"USD\n "
    price_list.append(item)
    return price_list


def print_price():
    downloading_data()
    print(f"Price of {chosen_crypto_name} is {float(chosen_crypto_price):.5f} [USD]")
    appending_sought_item_to_list()


def available_cryptos():
    print("""bitcoin\netherum\ndogecoin\nshibainu\nlitecoin""")


def single_crypto_data_log():
    global response_time
    with open("crypto log.txt", "a") as file:
        response_time = datetime.datetime.now().strftime("%d.%m.%Yr. %H:%M:%S")
        file.write(f"[{response_time}] {chosen_crypto_symbol}: {chosen_crypto_name} {float(chosen_crypto_price):.5f} "
                   f"USD\n ")


def sought_crypto_data_log():
    with open("crypto log.txt", "a") as file:
        file.writelines(price_list)


def menu():
    global price_list
    price_list = []
    action = input("""what u want to do?")
    - """)
    if action == "check price":
        print_price()
    elif action == "create log":

        print("\nFile with logs created.\n")
    elif action == "save sought scores":
        sought_crypto_data_log()
    else:
        print("Unknown action.")
        menu()


if __name__ == '__main__':
    print("     Welcome to my CRYPTO App! :)")
    downloading_data()


    input('Press ENTER to exit')
