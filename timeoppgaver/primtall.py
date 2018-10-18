while True:

    x = int(input("Skriv inn et heltall: "))

    svar = str(x) + ' er '
    divisor = 2
    while x > 1:
        while x % divisor == 0:
            x = x // divisor
            svar = svar + str(divisor)
            if x > 1:
                svar = svar + ' * '
        divisor = divisor + 1
    print(svar)

    if input('igjen? ') == 'j':
        continue
    else:
        break
