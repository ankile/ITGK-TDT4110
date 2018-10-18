# a)
def read_from_file(filename):
    f = open(filename, 'r')
    contents = f.read()
    f.close()
    return contents


# b)
def remove_symbols(text):
    characters = [',', '.', '!', '?', '%', '"', "'", '-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', '/', ';', '(', ')', '\n', '\t', '<', '>']
    new_word = ''
    for i in range(len(text)):
        okey = True
        for character in characters:
            if text[i] == character:
                okey = False
                break
        if okey:
                new_word += text[i].lower()

    words = new_word.split(' ')

    return words

#''.join(letter for letter in text if letter.isalpha() or letter == ' '

# c)
def count_words(filename):
    freq = {}

    for ord in filename:
        if ord not in freq:
            freq[ord] = 1
        else:
            freq[ord] += 1

    return freq

bible_dict = count_words(remove_symbols(read_from_file('BIBLE.txt')))
for word, value in bible_dict.items():
    print(word, value)