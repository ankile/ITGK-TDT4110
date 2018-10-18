import timeit


# Funksjon som regner ut neste faktor i rekken
def gjenbruk():
    if input("Igjen (j/n): ") == 'j':
        return True
    else:
        return False


def prod_funk(indeks):
    return 1+(1/(indeks**2))


# Hovedløkke for gjenbruk av programmet
while True:
    tol = float(input("Skriv in toleranse: "))

    start = timeit.default_timer()

    i = 0
    diff = 1
    prod = 1

    # Løkken beregningen gjøres i
    while not diff < tol:
        i += 1

        gammel_prod = prod
        prod = prod_funk(i) * prod

        diff = prod - gammel_prod

    # Printing av resultat
    print('Med en toleranse på %s, kjørte løkken %s ganger og endte med et produkt på %s' % (tol, i, prod))

    stop = timeit.default_timer()
    print(stop - start)

    # Spør om koden skal kjøres igjen
    if not gjenbruk():
        break




