"""
Program som tar variabler a, b og c, og vurderer hva slags, og hvor mange
løsninger en annengrads likning med de koeffisienter har.
"""

#While-løkke for gjenbruk
while True:
    print('Skriv inn verdier for a, b og c:')
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

#Beregning av d, med påfølgende sjekk av antall løsninger
    d = b**2-4*a*c
    beskjed = 'Likningen '+str(a)+'x^2 + '+str(b)+'x + '+str(c)
    if d == 0:
        print(beskjed, 'har kun en løsning')
    elif d > 0:
        print(beskjed, 'har to reelle løsninger')
    else:
        print(beskjed, 'har to imaginære løsninger')

#Sjekk om brukeren vil avslutte eller kjøre igjen
    if input('Igjen? ') == 'j':
        continue
    else:
        print('Avslutter...')
        break
