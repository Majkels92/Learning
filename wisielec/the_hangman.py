import hangman_stage
import random
import os
import string


def clear():
    os.system('cls')


def gain_words_from_text(text_file):  # gain list of words from text
    global pool_of_words
    pool_of_words = []
    with open(text_file, "r", encoding="UTF-8") as file:
        raw_txt = file.read()
    # deleting all numbers from text
    no_numbers_raw_text = raw_txt.translate(str.maketrans('', '', string.digits))
    # deleting all punctuation from text
    no_numbers_and_punctuation_raw_text = no_numbers_raw_text.translate(str.maketrans('', '', string.punctuation))
    words_of_raw_txt = set(no_numbers_and_punctuation_raw_text.replace("„", "").replace("”", "").replace("’", "").
                           lower().split())
    for word in words_of_raw_txt:
        if len(word) > 5:
            pool_of_words.append(word)
    return pool_of_words


def draw_game_word_from_pool():  # draw word from pool
    global word_letters, game_word
    word_letters = []
    game_word = random.choice(pool_of_words)
    for word_letter in game_word:
        word_letters.append(word_letter)
    return game_word


def hangman_failure_status():  # controls stage of gibbet and prints it
    if gibbet_status == 10:
        print(hangman_stage.stage_10)
        print(10 * "  GAME OVER !!!  ")
    else:
        print(hangman_stage.stage_list[gibbet_status])


def check_if_letter_in_word(picked_letter):  # checking if typed letter is in game word
    global gibbet_status
    if picked_letter in word_letters and picked_letter not in chosen_letters:
        print("CONGRATS WORD CONTAINS THAT LETTER")
        chosen_letters.append(picked_letter)
        counter = 0
        for i in word_letters:
            if i == picked_letter:
                display_string[counter] = word_letters[counter]
            counter += 1
    elif picked_letter in chosen_letters:
        print("YOU ALREADY PICKED THIS LETTER")
    else:
        print("NO MATCH FOUND :(")
        chosen_letters.append(picked_letter)
        gibbet_status += 1


def create_word_display(word_for_length):  # creates default display list with length of game word
    word_display_list = []
    for d in range(len(word_for_length)):
        word_display_list.append("_")
    return word_display_list


def display_word_progress(word_progress):  # display word with guessed letters
    print(" ".join(word_progress))


def menu():
    while gibbet_status != 10:
        letter = str(input("\nPlease type a letter which u want to check if it is in hidden word: "))
        clear()
        check_if_letter_in_word(letter)
        display_word_progress(display_string)
        hangman_failure_status()
        if "_" not in display_string:
            print("""
CONGRATULATIONS YOU WON !!!!
!!!!!!WINNER WINNER CHICKEN DINNER!!!!!!!""")
            break


if __name__ == '__main__':
    print("""WANNA PLAY A GAME?\n\nRules are simple, guess the word and u will survive....\n\n""")
    gibbet_status = 0
    pool_of_words = gain_words_from_text("text.txt")  # gain list of words from text
    game_word = draw_game_word_from_pool()  # draw word from pool
    chosen_letters = []
    display_string = create_word_display(game_word)  # creates display list
    display_word_progress(display_string)
    menu()
    input("press any key to exit")
    quit()
