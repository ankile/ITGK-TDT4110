def load_bin(filename):
    try:
        binstring = ''
        f = open(filename, 'r')
        for line in f:
            binstring += line.strip()

        return binstring

    except FileNotFoundError:
        print('Error: Could not open file "' + filename + '"')


# print(load_bin('binary-file.txt'))


def bin_to_dec(binary):
    dec = 0
    for i in range(len(binary)):
        dec += (2 ** (len(binary) - i - 1)) * int(binary[i])

    return dec


# print(bin_to_dec('11111111'))

def dec_to_char(dec):
    alfabet = ' ,.ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'

    if 0 <= dec <= 31:
        return alfabet[dec]
    else:
        return ''

# print(dec_to_char(31))

def bin_to_text(binstring):
    text = ''
    for i in range(0, len(binstring), 5):
        dec = bin_to_dec(binstring[i : i + 5])
        text += dec_to_char(dec)

    return text


# print(bin_to_text('0001100100001010011000111'))

def main():
    # 1
    print('Binary-to-text converter')

    # 2
    b_file = input('Name of binary file to load from: ')

    # 3
    b_string = load_bin(b_file)

    # 4
    txt = bin_to_text(b_string)

    # 5
    t_file = input('Name of text file to save to: ')

    # 6
    try:
        f = open(t_file, 'w')
        f.write(txt)
        f.close()

        # 7
        print(b_file, 'has been converted and saved to', t_file)

    except:
        print('Error: Could not write to file', t_file)


main()