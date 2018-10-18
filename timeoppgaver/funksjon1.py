def temperature():
    by = input("Hvor er du? ")
    temp = int(input("Hvor mange grader er det? "))

    if temp > 10:
        print("I", by, "er det sommervær.")
    elif temp > 0:
        print("I", by, "er det typisk Trønder-vær.")
    else:
        print("I", by, "er det kaldt vintervær.")


temperature()
