def gjennomsnitt(liste):
    total = 0
    for maling in malinger:
        total += maling
    total /= 3
    print("Gjennomsnittet av målingene er:", total)

m_1 = int(input('Første avmåling: '))
m_2 = int(input('Andre avmåling: '))
m_3 = int(input('Tredje avmåling: '))
malinger = [m_1, m_2, m_3]

gjennomsnitt(malinger)
