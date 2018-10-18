a = int(input('Skriv inn et heltall: '))
b = int(input('Skriv inn et til: '))

if a * b < a + b:
    print('Skriver ut summen av', a, 'ganget med', b, 'som er lik', a * b, 'siden det ble minst.')
else:
    print('Skriver ut summen av', a, 'lagt til', b, 'som er lik', a + b, 'siden det ble minst.')

print('Hva er 3*4?')
svar = int(input('Svar: '))

if svar == 12:
    print('Er ikke så dum som du ser ut du ;)')
else:
    print('Trist...')
