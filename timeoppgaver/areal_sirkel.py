import math

def areal_sirkel(r, pi):
    areal = pi * r ** 2
    print("Arealet er lik", round(areal,2))


R = int(input("radius: "))

areal_sirkel(R, math.pi)