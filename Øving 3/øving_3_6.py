print("Deloppgave a:")

n = 4
r = 0.5
i = 0
minSum = 0

while i <= n:
    minSum += r ** i
    i += 1

print("Summen av rekken er:", minSum, "\n")

print("Deloppgave b:")

tol = 0.001
minSum = 0
i = 0

while 2 - minSum > tol:
    minSum += r ** i
    i += 1

differanse = 2 - minSum
streng_1 = "Løkken kjørte " + str(i) + " ganger"
streng_2 = "\nDifferansen mellom grenseverdien av rekken og vår tilnærming er " + str(differanse)

print(streng_1, streng_2)
