while True:
    
    puls = int(input("Hva er pulsen din? "))

    if puls >= 80:
        print("Ro deg ned!")
    else:
        print("Bare slapp av")
        
    if input("Igjen? ") == "Ja":
        continue
    else:
        break
