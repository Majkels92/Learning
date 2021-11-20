import requests
import datetime


def help_available_cryptos():
    """Informs user about avaible cryptos."""
    print("""bitcoin\netherum\ndogecoin\nshibainu\nlitecoin""")


def downloading_data():
    """Downloads from server chosen crypto data."""
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


def response_time_from_server():
    """Return time of function call out, function used for determine time of action in App.
    The time for is delivered as: [13.11.2021r. 12:09:05][day.month.year hour.minute.second]"""
    time_log = datetime.datetime.now().strftime("%d.%m.%Yr. %H:%M:%S")
    return time_log


def appending_sought_item_to_list():
    global price_list
    """Appends searched price of crypto to list as string."""
    response_time = response_time_from_server()
    item = f"[{response_time}] {chosen_crypto_symbol}: {chosen_crypto_name} {float(chosen_crypto_price):.5f} "\
           f"USD"
    price_list.append(item)


def check_n_print_price():
    """Checks price of chosen crypto and appends that price to list to list"""
    downloading_data()
    print(f"Price of {chosen_crypto_name} is {float(chosen_crypto_price):.5f} [USD]")
    appending_sought_item_to_list()


def single_crypto_data_log():
    """Appends or creates file crypto log.txt with history of checked prices, represented as every record in new line.
    Every line contains time:crypto symbol:crypto name:crypto price with 5 numbers after decimal."""
    with open("crypto log.txt", "a") as file:
        response_time = response_time_from_server()
        file.write(f"[{response_time}] {chosen_crypto_symbol}: {chosen_crypto_name} {float(chosen_crypto_price):.5f} "
                   f"USD\n ")


def sought_crypto_data_log():
    """Transfers elements from list to txt file, after transfer clears list."""
    with open("crypto log.txt", "a") as file:
        for item in price_list:
            file.write(item+"\n")
    price_list.clear()


def menu():
    """Creates menu for App, function that controls App."""
    action = input("""I want to: """)
    if action == "check price":
        check_n_print_price()
        menu()
    elif action == "create log":
        single_crypto_data_log()
        print("\nFile with logs created/updated.\n")
        menu()
    elif action == "save scores":
        sought_crypto_data_log()
        menu()
    elif action == "exit":
        exit()
    elif action == "help":
        help_available_cryptos()
        menu()
    else:
        print("Unknown action.")
        menu()

price_list = []

if __name__ == '__main__':
    print("     Welcome to my CRYPTO App! :)"
    """what u want to do?")
        - check price of crypto type: check price
        - to check available cryptos type: help
        - create or append data of crypto price do file type: create log
        - save sought scores during running app and add to txt file, type: save scores
        - to exit app type: exit""")
    menu()
