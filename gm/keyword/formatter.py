def format_text():
    with open("words_not_formatted.txt", "r", encoding="utf8") as f:
        word_list = f.readlines()
    words = []
    for i in word_list:
        new_words = i.split("\t")
        words.append(new_words[1])
    return words
