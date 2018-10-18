print("Deloppgave a og b:\n")

k = int(input("Hvilket nummer i Fibonaccirekken vil du ha? "))
liste = [0, 1]

if k == 0:
    print("\nPå plass nummer 0 er tallet 0")
    print("Og summen er 0")
elif k == 1:
    print("På plass nummer 1 er tallet 1")
    print("Og summen er 1")
else:
    for i in range(2, k + 1):
        tall = liste[i - 1] + liste[i - 2]
        liste.append(tall)
    print("På plass nummer", k, "er tallet", liste[k])
    min_sum = 0
    for i in liste:
        min_sum += i
    print("Og summen er", min_sum)

print("\nDeloppgave c:")

print("\nHer er alle tallene opp til og med k=" + str(k) + ":")
print(liste)