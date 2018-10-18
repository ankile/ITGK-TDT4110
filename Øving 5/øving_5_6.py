# Deloppgave a)
print("Oppgave a)")


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True


def weekday_newyear(year):
    weekdays = ['man', 'tir', 'ons', 'tor', 'fre', 'lor', 'son']
    day = 0
    for i in range(1900, year + 1):
        #print(i, weekdays[day % 7])
        if is_leap_year(i):
            day += 2
        else:
            day += 1


weekday_newyear(1919)


# Deloppgave b)


def is_workday(day):
    if day % 7 == 5 or day % 7 == 6:
        return False
    else:
        return True


print("")
# Deloppgace c)
print("Oppgave c)")


def workdays_in_year(year):
    for i in range(1900, year + 1):
        work_days = 0
        day = weekday_newyear(i)

        if is_leap_year(i):
            days_in_year = 366
        else:
            days_in_year = 365

        for j in range(day, days_in_year + day + 1):
            if is_workday(j):
                work_days += 1
            day += 1

        print("%s har %s arbeidsdager" % (i, work_days))


workdays_in_year(1919)
