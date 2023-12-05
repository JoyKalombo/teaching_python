text = "This is really awesome right now"
word_lengths = text.split(" ")
longest = "00"
counter = 0

def longest_even_word(text):
    global longest, counter

    for i in word_lengths:
        if (len(i) % 2 == 0) and (len(i) > counter):
            counter = len(i)
            longest = i

    print(longest, counter)

longest_even_word(text)