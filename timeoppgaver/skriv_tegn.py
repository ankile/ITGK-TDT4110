def skriv_tegn_indeks(tekst, tegn):
    antall = []
    for i in range(len(tekst)):
        if tekst[i].lower() == tegn.lower():
            antall.append(i)
    return antall

print(skriv_tegn_indeks('Lars Lien Ankile', 'e'))
