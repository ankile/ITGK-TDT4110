from word_list import *

def checkin():
    print('Hi, please tell me how you are feeling. Feel free to quit anytime, just write "x".')
    user_input = input()
    if user_input.lower() == 'x':
        return False

    write_to_file(user_input, 'user_answers.txt')
    return user_input.split(' ')

def write_to_file(text, file):
    f = open(file, 'a')
    f.write(text + '\n')
    f.close()


def main():
    while True:
        user_list = checkin()
        if not user_list:
            break

        mood_qotient = 0
        neutral = False
        for word in user_list:
            if word in neutral_words:
                neutral = True
            for key in words:
                if word.lower() == key:
                    mood_qotient += words[key]


        print(mood_qotient)


main()
