total = 0
for x in range(1,101):
    total += x

print("Summen av de første 100 tallene ble", total)

produkt = 1
teller = 1
count = 0
while not produkt > 1000:
    produkt *= teller
    teller += 1
    count += 1
    print(produkt)
print("Løkken kjørte", count, "ganger og produktet ble", produkt)

svar = ""
while svar != 12:
    svar = int(input("Hva er 3*4? "))
    if svar == 12:
        print("Det stemmer!")
    else:
        print("Feil")
