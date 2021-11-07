import hangman_stage
import random


def gain_words_from_text(text_file): #gain list of words from text
    pool_of_words = []
    with open(text_file, "r", encoding="UTF-8") as file:
        raw_txt = file.read()
    words_of_raw_txt = set(raw_txt.replace("?", "").replace("!", "").replace(",", "").replace(".", "").lower().split())
    for word in words_of_raw_txt:
        if len(word) > 5:
            pool_of_words.append(word)
    return pool_of_words

def draw_game_word_from_pool(): #draw word from pool
    global word_letters
    word_letters = []
    game_word = random.choice(pool_of_words)
    for word_letter in game_word:
        word_letters.append(word_letter)
    return game_word

def hangman_failure_status(): #controls stage of gibbet and prints it
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

def check_if_letter_in_word(picked_letter): #checking if typed leter is in game word
    global gibbet_status
    if picked_letter in word_letters and picked_letter not in chosen_letters:
        print("CONGRATS WORD CONTAINS THAT LETTER")
        chosen_letters.append(picked_letter)
        counter = 0
        for i in word_letters:
            if i == picked_letter:
                display_string[counter] == word_letters[counter]
            counter +=1
    elif picked_letter in word_letters and picked_letter in chosen_letters:
        print("YOU ALREADY PICKED THIS LETTER")
    else:
        print("NO MATCH FOUND :(")
        gibbet_status += 1
        hangman_failure_status()

def create_word_display(game_word): #creates default display list with lenght of game word
    word_display_list = []
    for d in range(len(game_word)):
        word_display_list.append("_")
    return word_display_list

def display_word_progress(word_progress): #display word with guessed letters
    print(" ".join(word_progress))

def menu():
    while gibbet_status != 10:
        letter = input("\nPlease type a letter which u want to check if it is in hidden word: ")
        check_if_letter_in_word(letter)
        display_word_progress(display_string)
if __name__ == '__main__':
    print("""WANNA PLAY A GAME?\n\nRules are simple, guess the word and u will survive....\n\n""")
    gibbet_status = 0
    pool_of_words = gain_words_from_text("text.txt") #gain list of words from text
    game_word = draw_game_word_from_pool() #draw word from pool
    chosen_letters = []
    display_string = create_word_display(game_word) #creates display list
    print(game_word)
    menu()



