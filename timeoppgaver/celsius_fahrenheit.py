def c2f():
    c = int(input("Temperatur i celsuis: "))
    print(c, "grader celsius er", round((c * 9 / 5) + 32, 1), "grader Fahrenheit.")


def f2c():
    f = int(input("Temperatur i Fahrenheit: "))
    print(f, "grader fahrenheit er", round((f - 32) * 5 / 9, 1), "grader celsius")


def main():
    c2f()
    f2c()


main()
