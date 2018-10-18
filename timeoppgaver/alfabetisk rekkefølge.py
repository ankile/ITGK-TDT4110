while True:

    val_1 = input('Skriv inn en streng: ')
    val_2 = input('Skriv inn en til: ')

    if val_1 == val_2:
        print('Begge inputs er like')
    elif val_1 < val_2:
        print(val_1, 'kommer før', val_2, 'i alfabetet')
    else:
        print(val_2, 'kommer før', val_1, 'i alfabetet')

    if input('Igjen? ') == 'j':
        continue
    else:
        break
