# Velkomstbeskjed
def velkomstbeskjed():
    print(' Velkommen til hybelregnskapsprogram v.6.4.11 ')
    print('==============================================\n')


# Skriv meny (returnerer valget brukeren gjor)
def skriv_meny():
    print('Velg kommando [utgift|inntekt|vis|load|fjern|avslutt]')
    return input('--> ')


# Registrere inntekt/utgift
def registrer(dictionary, dbid, valg):
    dato = input('Dato [yyyy-mm-dd')
    belop = float(input('Belop: [kr] '))
    beskrivelse = input('Beskrivelse: ')
    if valg == 'utgift':
        belop = (-1) * belop

    dictionary[dbid] = [dato, belop, beskrivelse]
    melding('Data er registrert')
    return dictionary


def vis(dictionary):
    balanse = 0
    header = 'ID'.rjust(4) + ' ' + 'Dato'.ljust(11) + ' ' + 'Beskrivelse'.ljust(30) + ' ' + 'Sum'
    print(header)
    print('=' * 55)
    for key in dictionary:
        s = str(key).rjust(4) + ' ' + dictionary[key][0].rjust(11) + ' '
        s += dictionary[key][2].ljust(30) + ' ' + str(dictionary[key][1]).rjust(8)
        print(s)
        balanse += dictionary[key][1]  # Oppdater balansen

    print('Balanse:', balanse)


def fjern(dictionary):
    print('IDer i databasen:', dictionary.keys())
    dbid = int(input('IDen som skal fjernes: '))
    if dbid in dictionary:
        del dictionary[dbid]
        melding('Innslag fjernet')
    else:
        melding('Det innslaget finnes ei.')

    return dictionary


def velg_filnavn():
    return input('Velg filnavn: ')


def melding(beskjed):
    print('-->', beskjed)
