import math


# Deloppgave a

def f(x):
    return (x - 12) * math.exp(5 * x) - (8 * ((x + 2) ** 2))


def g(x):
    return (-x) - 2 * (x ** 2) - 5 * (x ** 3) + 6 * (x ** 4)


# Deloppgave b
def derivate(h, x, func):
    return (func(x + (h / 2)) - func(x - (h / 2))) / (h)


# Deloppgave c
def newtons_method(h, x, func, tol):
    diff = 1
    i = 0
    gammel_x = x
    while diff > tol:
        ny_x = gammel_x - ((func(gammel_x))/(derivate(h, gammel_x, func)))

        diff = math.fabs(ny_x - gammel_x)

        gammel_x = ny_x

        i += 1
    return round(ny_x, 2), x

print("Funksjonen f: x = %s, for startverdi %s" % (newtons_method(0.00000001, -2, f, 0.0000000001)))
print("Funksjonen g: x = %s, for startverdi %s" % (newtons_method(0.00000001, 1, g, 0.0000000001)))
print("Funksjonen g: x = %s, for startverdi %s" % (newtons_method(0.00001, -1, g, 0.00001)))