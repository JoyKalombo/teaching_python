def replace_word(paragraph, old_word, new_word):
    word_list = paragraph.split()
    for i in range(len(word_list)):
        if word_list[i] == old_word:
            word_list[i] = new_word
    new_paragraph = ' '.join(word_list)
    return new_paragraph
 
Paragraph = "I like eating food with my friends when we go to parties."
Old_word = "food"
New_word = "cars"
funny_paragraph = replace_word(Paragraph, Old_word, New_word)
print(funny_paragraph)

# We will start developing a small application