# a)
def write_to_file(data):
    f = open('my_file.txt', 'a')
    f.write(data + '\n')
    f.close()


# b)
def read_from_file(filename):
    f = open(filename, 'r')
    print(f.read())


# c)
def main():
    while True:
        try:
            answer = input('Vil du lese eller skrive? (r/w): ')
            if answer.lower() == 'done':
                break
            elif answer == 'r':
                read_from_file('my_file.txt')
            elif answer == 'w':
                user_input = input('Hva vil du skrive til filen? ')
                write_to_file(user_input)
            else:
                print('Ugyldig input...')
                continue

        except IOError:
            print('Den filen finnes ikke...')
            continue

main()