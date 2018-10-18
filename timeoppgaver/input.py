navn = input("Hva heter du? ")
alder = input("Hei " + navn + ", hvor gammel er du? ")

print("Du heter", navn, "og er", alder,\
      "år gammel, hvilket betyr at du ble født i", str(2017 - int(alder))\
      + ", og kommer til å være", int(alder) + 10, "år om 10 år.")
