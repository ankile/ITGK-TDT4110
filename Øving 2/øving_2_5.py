def rabatt(tid):
    if alder < 16:
        print ("Som barn under 16 får du 50% rabatt på fullprisbiletter, og din pris blir 220,-")
    elif type_passasjer == 'S' or type_passasjer == 'M' or type_passasjer == 'H':
        print ("Som militær/student/honnør får du 25% rabatt av fullpris, og din pris blir 330,-")
    else:
        if tid == 1:
            print ("Da tilbyr vi fullprisbiletter til 440,-")
        else:
            print ("For sent for minipris, du må betale fullpris: 440,-")

while True:
    dager = input("Hvor mange dager er det til avreise? ")
    alder = int(input("Hvor gammel er du? "))
    type_passasjer = input("Er du student (S), militær (M) eller honnør (H)? ")

# Sjekk om input er et tall
    if dager.isdigit():
        dager = int(dager)
    else:
        print("Hold deg til tall..")
        continue

# Avgjørelse av bilettpris
    if dager >= 14:
        print ("Du kan få minipris: 199,-, men disse kan ikke refunderes, ønsker du minipris? (J/N)")
        if input() == 'J':
            print ("Takk for pengene, god reise!")
        else:
            rabatt(0)
    else:
        rabatt(1)

    if input('igjen? ') == 'j':
        continue
    else:
        break
