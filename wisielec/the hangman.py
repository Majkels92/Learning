def gain_words_from_text(text_file):
    global pool_of_words
    with open(text_file, "r", encoding="UTF-8") as file:
        raw_txt = file.readline()
    raw_txt_list = raw_txt.split()
    pool_of_words = []
    for word in raw_txt_list:
        if len(word) >= 5 and not word == word.capitalize():
            pool_of_words.append(word)

gain_words_from_text("text.txt")
print(pool_of_words)