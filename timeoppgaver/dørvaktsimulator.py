while True:
    print('Hei, jeg er THE DOORMAN!')
    navn = input('Hva heter du? ')
    alder = int(input('Okey ' + navn + ', hvor gammel er du? '))

    if alder < 18:
        print('Du er for ung,', navn)
    else:
        print('Du er gammel nok')
        full = input('Men er du for full? ')
        if full == 'ja':
            print('Du slipper ikke inn, for du er for full!')
        else:
            print('Velkommen inn', navn)
    if input('Igjen? ') == 'j':
        continue
    else:
        break
