SKILTBOKSTAV = ('A','B','C','D','E','F','G','H','J','K','L','N','P','R','S','T','U','V','X','Y','Z','?')


def fil_til_dict(filename):
    try:
        f = open(filename, 'r')
        content = f.readlines()
        f.close()
        print('Fil lest', end='\n\n')

    except:
        print('En feil har oppstått under lasting av fil...')
        return False

    for i in range(len(content)):
        content[i] = content[i].strip()
        content[i] = content[i].split()

    ordbok = {}
    for line in content:
        ordbok[line[0]] = [line[1], line[2], line[3], line[4], line[0]]
    return ordbok


def les_inn_bilinfo():
    result = [] + [input('Hvilket bilmerke var det? ')]
    result += [input('Hvilken modell? ')]
    return result + [input('Hvilken farge? ')]


def les_gyldig_vitneskilt():
    while True:
        skilt = input('Skriv inn skiltnummer, bruk "?" der du er usikker: ')

        if len(skilt) != 7:
            print('Skilnummer må være 7 langt.')
            continue

        if skilt[0] not in SKILTBOKSTAV or skilt[1] not in SKILTBOKSTAV:
            print('De to første tegnene må være bokstaver må være bokstav eller "?"')
            continue

        error = False
        for i in range(2, 7):
            if not skilt[i].isdigit() and skilt[i] != '?':
                print('De siste fem må være tall eller "?"')
                error = True
                break
        if error:
            continue

        return skilt


def skriv_til_skjerm(regnummer, oppslag):
    if len(regnummer) == 0:
        print('Ingen mathcer..', end='\n\n')
    else:
        print('Mulig(e) kjøretøyer:')
        for nummer in regnummer:
            print(nummer, 'Eier:', oppslag[nummer][3])
        print()


def match(vitne, politi):
    for i in range(len(vitne)):
        if vitne[i] != politi[i] and vitne[i] != '?':
            return False
    return True


def match_liste(vitne, politi_liste):
    matches = []
    for skilt in politi_liste:
        if match(vitne, skilt):
            matches.append(skilt)
    return matches
