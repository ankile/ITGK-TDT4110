def alle_deltagere(lister):
    # INPUT: ei liste av lister, hvor hver indre liste inneholder navn
    #        på deltagere som har besøkt et visst punkt av interesse
    # OUTPUT: returnerer mengden av deltagere som har vært på minst ett sted
    # ??? TBD skriv koden din her
    minst_en = []
    for liste in lister:
        minst_en.extend(liste)
    return set(minst_en) # ? TBD returner noe fornuftig

def ivrigste_deltagere(lister):
    # INPUT: en liste av lister, hvor hver indre liste inneholder navn
    #        på deltagere som har besøkt et visst punkt av interesse
    # OUTPUT: returnerer mengden av deltagere som har vært på alle stedene
    # ??? TBD skriv koden din her
    deltakere  = set(lister[0]) & set(lister[1]) & set(lister[2])
    return deltakere # ? TBD returner noe fornuftig

def main():
    fjell_lister =  [['Jo', 'Ine', 'Eli', 'Bo', 'Ron', 'Sam', 'Una', 'Ron'],
                     ['Eli', 'Ada', 'Oda', 'Jo', 'Dag', 'Una', 'Ron'],
                     ['Bo', 'Ada', 'Tor', 'Dag', 'Jo', 'Eli', 'Frank']]
    print('Alle deltagere (minst ett fjell):',
          alle_deltagere(fjell_lister) )
    ant_fjell = len(fjell_lister)
    print('Vært på alle', ant_fjell, 'fjell:',
          ivrigste_deltagere(fjell_lister) )

main()
