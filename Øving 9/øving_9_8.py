f = open('poenggrenser_2011.csv', 'r')
poeng_grenser = f.readlines()

print(poeng_grenser[0][-6:-2])


# a)
def alle_søkere(studier):
    teller = 0
    for studie in studier:
        if studie[-6:-2] == 'Alle':
            teller += 1

    return teller


print(alle_søkere(poeng_grenser))

# b)
def gjennomsnitt_ntnu(studier):
    total = 0
    teller = 0
    for grense in studier:
        if grense[1:5] == 'NTNU' and not grense[-6:-2] == 'Alle':
            for i in range(len(grense)):
                if grense[i] == ',':
                    teller += 1
                    total += float(grense[i + 1:])

    return total/teller


print(gjennomsnitt_ntnu(poeng_grenser))


# c)
def lavest_snitt(studier):
    midlertidig_laveste_navn = ''
    midlertidig_laveste = 100
    for grense in studier:
        if not grense[-6:-2] == 'Alle':
            for i in range(len(grense)):
                if grense[i] == ',':
                    if float(grense[i + 1:]) < midlertidig_laveste:
                        midlertidig_laveste = float(grense[i + 1:])
                        midlertidig_laveste_navn = grense[1:i]

    return midlertidig_laveste_navn, midlertidig_laveste


print(lavest_snitt(poeng_grenser))

