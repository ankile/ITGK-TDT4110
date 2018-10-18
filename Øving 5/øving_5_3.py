# Deloppgave a

# Definerer funksjonene som returnerer billettprisen
def billettpris(alder, sykkel):

    if alder < 5:
        pris = 0
    elif 4 < alder < 21:
        pris = 20
    elif 20 < alder < 26:
        pris = 50
    elif 25 < alder < 61:
        pris = 80
    elif alder > 60:
        pris = 0
    else:
        return False

    # Deloppgave b
    if sykkel == 'j':
        pris += 50

    return pris

# Deloppgave c
while True:
    kundealder = int(input("Hvor gammel er du? "))
    kunde_sykkel = input("Har du med sykkel? (j/n) ")

    subtotal = billettpris(kundealder, kunde_sykkel)

    print("Din pris blir %s,-. God reise!" % (subtotal))

    if input("Ønsker du kjøpe flere biletter? (j/n) ") == 'j':
        continue
    else:
        break
