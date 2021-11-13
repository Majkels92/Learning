import random


def general_func_for_lotto(amount, totalamount):
    random_list = random.sample(range(1, totalamount + 1), amount)
    print(random_list)


def duze_lotto():
    random_list = random.sample(range(1, 50), 6)
    print(random_list)


def mini_lotto():
    random_list = random.sample(range(1, 43), 5)
    print(random_list)


def system_4_mini():
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
    bets = []
    for j in range(8):
        bet = []
        for i in range(5):
            x = random.choice(list_of_numbers)
            list_of_numbers.remove(x)
            bet.append(x)
        bets.append(bet)
    for k in range(1, 9):
        print(f"Lottery ticket number {'k'}:", bets[0])

if __name__ == '__main__':
    system_4_mini()
    input("press any key to exit")
