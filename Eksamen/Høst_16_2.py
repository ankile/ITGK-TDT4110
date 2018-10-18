D = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',6: 'six',7: 'seven', 8: 'eight', 9: 'nine',
     10: 'ten',11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',15: 'fifteen', 16: 'sixteen',
     17: 'seventeen',18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',40: 'forty', 50: 'fifty',
     60: 'sixty', 70: 'seventy',80: 'eighty', 90: 'ninety'}

L = [1000000, ' million', 1000, ' thousand', 1, '']

def i2_txt(tall):
    if tall in D:
        return D[tall]
    else:
        return D[tall//10 * 10] + '-' + D[tall%10]


def i3_txt(tall):
    output = ''
    rest = tall % 100
    if tall >= 100:
        output = D[tall // 100] + ' hundred'

        if rest > 0:
            output += ' '

    if rest > 0:
        output += i2_txt(rest)

    return output


def i9_txt(tall):
    output = ''
    rest = tall % 1000000

    if tall >= 1000000:
        output += i3_txt(tall // 1000000) + ' million'
        if rest > 0:
            output += ' '

    if rest >= 1000:
        output += i3_txt(rest // 1000) + ' thousand'
        rest = rest % 1000
        if rest > 0:
            output += ' '

    output += i3_txt(rest)

    return output


# print(i9_txt(12000))


def listify(string):
    liste = string.split()
    index_numbers = []

    for number in liste:
        if number.isdigit():
            index_numbers.append(liste.index(number))
    return liste, index_numbers


def add_words(string):
    ord_liste, index = listify(string)

    for i in range(len(index)):
        ord_liste[index[i]] += ' - ' + i9_txt(int(ord_liste[index[i]])) + ' -'

    return ' '.join(ord_liste)

print(add_words('C owes 91 pounds to D and 55 pounds to E for stealing 100 dollars, after eating 123000 kroners'))
print(add_words('The evildoer is hereby fined 945000000 yen'))
print(add_words('Mr.X shall pay 9005100 dollars'))

