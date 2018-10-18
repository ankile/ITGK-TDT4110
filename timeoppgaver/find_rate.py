def find_rate(filename, check_rate, acc):
    f = open(filename, 'r')
    for line in f:
        line = line.strip()
        liste = line.split()
        rate = float(liste[1])
        if round(check_rate, acc)== round(rate, acc):
            print(liste[0] + ':', rate)


find_rate('USD_NOK.txt', 6.2, 2)