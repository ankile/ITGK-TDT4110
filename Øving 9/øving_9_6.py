# a)
def number_of_lines(filename):
    f = open(filename, 'r')
    lines = len(f.readlines())
    f.close()
    return lines

print(number_of_lines('numbers.txt'), '\n')

# b)
def number_frequency(filename):
    f = open(filename, 'r')
    numbers = f.readlines()

    frequency = {}

    for number in numbers:
        number = int(number)

        if number not in frequency.keys():
            frequency[number] = 1
        else:
            frequency[number] += 1

    f.close()
    return frequency


for item in number_frequency('numbers.txt').items():
    print(item)