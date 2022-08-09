import random


def general_func_for_lotto(amount, total_amount):
    random_list = random.sample(range(1, total_amount + 1), amount)
    return random_list


def duze_lotto():
    random_list = random.sample(range(1, 50), 6)
    return random_list


def mini_lotto():
    random_list = random.sample(range(1, 43), 5)
    return random_list


def system_4_mini():
    list_of_numbers = []
    for numb in range(42):
        list_of_numbers.append(numb+1)
    print(list_of_numbers)
    bets = []
    for j in range(8):
        bet = []
        for i in range(5):
            x = random.choice(list_of_numbers)
            list_of_numbers.remove(x)
            bet.append(x)
        bets.append(bet)
    return bets


def menu():

    choice = input("""Choose your bet (type number):
    1. Duże lotto
    2. Mini lotto
    3. System mini lotto
    
    I am choosing: """)
    if choice == '1':
        result = duze_lotto()
        print(result)
    elif choice == '2':
        result = mini_lotto()
        print(result)
    elif choice == '3':
        result = system_4_mini()
        for k in range(1, 9):
            print(f"Lottery ticket number {k}:", sorted(result[k-1]))
    else:
        print("Can't find function, try again: ")
        menu()


if __name__ == '__main__':
    menu()
    ending_program = input("press any key to exit")
