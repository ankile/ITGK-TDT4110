from K15_hjelpefunksjoner import *


def main():
    igjen = 'J'
    oppslag = fil_til_dict('biler.txt')

    if oppslag == False:
        return False

    while igjen == 'J':
        bilinfo = les_inn_bilinfo()
        skiltinfo = les_gyldig_vitneskilt()
        matches = []
        alle_biler = []
        for key in oppslag:
            alle_biler.append(oppslag[key])

        for i in range(len(alle_biler)):
            if match(bilinfo, alle_biler[i]):
                matches.append(alle_biler[i][4])

        matches = match_liste(skiltinfo, matches)

        skriv_til_skjerm(matches, oppslag)

        igjen = input('Igjen? (J/N) ')

main()