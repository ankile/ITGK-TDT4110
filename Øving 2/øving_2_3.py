# a)
# tall_1, tall_2 og resultat er alle eksempler opå variabler, hvor tall_1
# holder et heltall, tall_2 holder en streng, og resultat går ikke fordi
# heltallsdivisjon med en tekstreng funker ikke.

# b)
# While-løkke av gjenbrukshensyn
while True:
    tall_1 = 2

# Her er det lagt til en int() for å få heltallsdivisjon til å fungere (feil 1)
    tall_2 = int(input("Skriv inn et tall: "))
# Denne if-en sjekker om tall_2 er 0, og gjennomfører divisjon om det ikke er
# eller sender bruker tilbake til start om det er null
    if tall_2 == 0:
        print('Du kan ikke dele på 0, vennligst prøv igjen')
        continue
    else:
        resultat = tall_1 // tall_2
        print(tall_1, 'delt på', tall_2, 'ble:', resultat)

# Restartprompt
        if input('igjen? ') == 'j':
            continue
        else:
            break

# c)
# Igjen av gjenbrukshensyn
while True:
    a = int(input('Skal a være lik 2 eller 3? '))
    b = 3
    if (b<a or not b%a):
        b = a+b
    else:
        a = a*b
    print("a: ",a)
    print("b: ",b)

# Restartprompt
    if input('igjen? ') == 'j':
        continue
    else:
        break

# Ved a=2 vil b<a = False, og b%a=1, som betyr True, men med not foran blir det
# False, så den hopper til else-en og ganger a med b -> 2*3=6, og vil printe
# a=6 og b=3.
#
# Ved a=3 vil b<a fortsatt være False, men b%a=0, hvilket er False, og med not
# foran blir den true, og if-en tilfredstilles, a+b=6, og programmet skriver
# a=3 og b=6.
