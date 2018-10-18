from time import sleep


def show_display(content):
    print()
    if len(content) == 6 and len(content[0]) == 30:
        print("####################################")
        print("#                                  #")
        for row in content:
            print('#  ' + row.upper() + "  #")
        print("#                                  #")
        print("####################################")
    else:
        print("Error: Wrong dimensions")


def enter_line(prompt, length):
    sentence = ''

    while len(sentence) != length:
        sentence = input(prompt + ': ')
        if len(sentence) != length:
            print('Input must be', length, 'characters long.')

    return sentence


# print(enter_line('Please input string', 6))


def adjust_string(text, length):

    if len(text) > length:
        text = text[:length]
    elif len(text) < length:
        tall = length//2 - len(text)//2
        return ' '*(length-tall-len(text)) + text + ' '*tall
    return text

# print(adjust_string('12345', 6))


def enter_line_smart(prompt, length):
    sentence = input(prompt + ': ')
    sentence = adjust_string(sentence, length)
    return sentence


# print(enter_line_smart('Gi meg en linje a', 5))


def enter_show_text():
    liste = []
    for i in range(6):
        text = input('Line ' + str(i+1) + ': ')

        text = adjust_string(text, 30)

        liste.append(text)

    show_display(liste)

# enter_show_text()


def scroll_display(content, line):
    for i in range(30):
        show_display(content)
        content[line - 1] = content[line - 1][1:] + content[line - 1][0]
        sleep(0.1)

    show_display(content)


content = ['Dette er en linje med tekst so',
           '='*30,
           'Dette er en linje med tekst so',
           'Dette er en linje med tekst so',
           'Dette er en linje med tekst so',
           'Dette er en linje med tekst so']

# scroll_display(content, 3)

def display_from_file(filename):
    f = open(filename)
    content = f.readlines()
    f.close()

    for i in range(len(content)):
        content[i] = content[i].rstrip()

    for i in range(len(content)):
        content[i] = adjust_string(content[i], 30)

    for i in range(0, len(content), 6):
        show_display(content[i:i + 6])
        sleep(5)





display_from_file('message.txt')
