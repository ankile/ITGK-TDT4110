# Karaktergrense

# For flere gjennomkkjøringer
while True:
    poeng = input('Hvor mange poeng fikk du? ')

# Sjekker om input er et heltall
    if not poeng.isdigit():
        print('Hold deg til tall')
        continue

# Siden poeng er et heltall kan det konverteres og sjekkes for verdi
    poeng = int(poeng)
    if poeng < 0 or poeng > 100:
        print('Hold deg innenfor 0 til 100 poeng')
        continue

# Siden poeng er et heltall mellom 0 og 100 kan vi sjekke Karaktergrense
    if poeng > 88:
        print('Gratulerer, du fikk A')
    elif poeng > 76:
        print('Gratulerer, du fikk B')
    elif poeng > 64:
        print('Det ble en C')
    elif poeng > 52:
        print('Ble dessverre en D')
    elif poeng > 40:
        print('Oioi, gikk ikke helt veien det her, ble dessverre E')
    else:
        print('Kan vel ikke bli mye verre enn E?')

# Sjekk om bruker vil kjøre programmet igjen
    if input('igjen? ') == 'j':
        continue
    else:
        break
