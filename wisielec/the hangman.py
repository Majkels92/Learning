import hangman_stage
import random


def gain_words_from_text(text_file):
    with open(text_file, "r", encoding="UTF-8") as file:
        raw_txt = file.readline()
    raw_txt_list = raw_txt.split()
    pool_of_words = []
    for word in raw_txt_list:
        if len(word) > 5 and word != word.capitalize() and "-" not in word:
            pool_of_words.append(word)
    return pool_of_words

def draw_game_word_from_pool():
    game_word = random.choice(pool_of_words)
    return game_word

"""def menu():
    while gibbet_status != 10:
        letter = input("\nPlease type a letter which u want to check if it is in hidden word: ")
        if letter is in game_word"""

def hangman_failure_status():
    if gibbet_status == 0:
        pass
    elif gibbet_status == 1:
        print(hangman_stage.stage_1)
    elif gibbet_status == 2:
        print(hangman_stage.stage_2)
    elif gibbet_status == 3:
        print(hangman_stage.stage_3)
    elif gibbet_status == 4:
        print(hangman_stage.stage_4)
    elif gibbet_status == 5:
        print(hangman_stage.stage_5)
    elif gibbet_status == 6:
        print(hangman_stage.stage_6)
    elif gibbet_status == 7:
        print(hangman_stage.stage_7)
    elif gibbet_status == 8:
        print(hangman_stage.stage_8)
    elif gibbet_status == 9:
        print(hangman_stage.stage_9)
    elif gibbet_status == 10:
        print(hangman_stage.stage_10)
        print(10 * "  GAME OVER !!!  ")


if __name__ == '__main__':
    print("""WANNA PLAY A GAME?\n\nRules are simple, guess the word and u will survive....\n\n""")
    gibbet_status = 0
    pool_of_words = gain_words_from_text("text.txt")
    game_word = draw_game_word_from_pool()
    print(pool_of_words)
    print(game_word)



