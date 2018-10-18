ALDER_MIN = 16
ALDER_MAX = 25

antall_kvinner = 0
antall_menn = 0
antall_fag = 0
antall_itgk = 0
antall_timer_lekser = 0
antall_personer = 0
total_alder = 0


# Delfunksjoner
def print_velkomstinfo():
    print('Hei, og velkommen til den store spørreundersøkelsen!')
    print('Under kommer en rekke spørsmål vi håper du vil besvare.')
    print('Om du ønsker å avslutte er det bare å svare "hade" på et hvilket som helst spørsmål.')


def sjekk_hade(streng):
    if streng == 'hade':
        return True


def les_ja_nei(spm):
    if spm == 'j' or spm == 'n':
        return True
    else:
        return False


def skriv_statistikk():
    print('Etter endt undersøkelse sitter vi igjen med følgende statistikk:\n')

    print('%s person(er) deltok på undersøkelse, med en total alder på %s år, altså en gjennomsnittlig alder på %s år.'
                                                         % (antall_personer, total_alder, total_alder/antall_personer))
    print('Av disse er %s menn og %s kvinner. \n' % (str(antall_menn), str(antall_kvinner)))

    print('Av de %s personene som deltok har %s fag, og %s har ITGK.' % (antall_personer, antall_fag, antall_itgk))
    print('Til sammen bruker de %s timer daglig på lekser, som blir et gjennomsnitt på %s.' % (antall_timer_lekser,
                                                                                antall_timer_lekser/antall_personer))
    print('slutt.')


# Hovedfunksjonen
def main(kvinner, menn, ant_fag, itgk, lekser, personer, tot_alder):

    while True:

        print_velkomstinfo()

        # Spør om kjonn
        kjonn = input("Er du mann eller kvinne? (f/m) ")
        if sjekk_hade(kjonn):
            break

        # Spør om alder
        alder = input("Hvor gammel er du? ")
        if sjekk_hade(alder):
            break

        alder = int(alder)

        # Sjekk om personen kvalifiserer
        if alder < ALDER_MIN or alder > ALDER_MAX:
            print('Beklager, du hører ikke til målgruppen for denne undersøkelsen.')
            continue

        # Hvis alder er godkjent, oppdater statistikken
        tot_alder += alder
        personer += 1

        # Lagre kjønnet i databasen
        if kjonn == 'f':
            kvinner += 1
        if kjonn == 'm':
            menn += 1

        # Sjekk hvorvidt personen tar fag
        while True:
            fag = input('Tar du fag? (j/n) ')
            if sjekk_hade(fag):
                break

            if les_ja_nei(fag):
                if fag == 'j':
                    ant_fag += 1
                break
            else:
                continue
        if sjekk_hade(fag):
            break

        # Sjekk om studenten tar ITGK, avhengig av alder
        if alder < 22:
            medlem_itgk = input('Tar du ITGK? (j/n) ')
        else:
            medlem_itgk = input('Tar virkelig du ITGK? (j/n) ')

        if sjekk_hade(medlem_itgk):
            break
        # Om personen tar ITGK, oppdater statistikk
        if medlem_itgk == 'j':
            itgk += 1

        # Spør om antall timer lekser per dag
        timer_lekser = int(input('Hvor mange timer bruker du i snitt per dag på lekser? '))

        # Legg til antall timer i totalen
        lekser += timer_lekser

        # Spør om brukeren vil kjøre ny undersøkelse
        if input('igjen? (j/hade) ') == 'hade':
            break
        else:
            continue

    return kvinner, menn, ant_fag, itgk, lekser, personer, tot_alder


antall_kvinner, antall_menn, antall_fag, antall_itgk, antall_timer_lekser, antall_personer, total_alder = \
    main(antall_kvinner, antall_menn, antall_fag, antall_itgk, antall_timer_lekser, antall_personer, total_alder)

skriv_statistikk()

# Siden vi ikke lagrer resultatene i en fil, permanent på harddisk, vil dataene gå tapt når programmet avsluttes, og
# kan derfor ikke hentes ut igjen. Dette er fordi alle variabler som lagres underveis lagres kun i minnet, altså i RAM,
# som er volatilt og dermed blir borte når vi avslutter.