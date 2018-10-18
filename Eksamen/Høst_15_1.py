def read_time_1():

    hour_bool = minute_bool = second_bool = False
    time = []

    while not (hour_bool and minute_bool and second_bool):

        if not hour_bool:
            hour = int(input('Enter hour: '))
            if hour < 0 or hour > 23:
                print('Hour must be between 0 and 23.')
                continue
            else:
                time.append(hour)
                hour_bool = True

        if not minute_bool:
            minute = int(input('Enter minute: '))
            if minute < 0 or minute > 59:
                print('Minute must be between 0 and 59.')
                continue
            else:
                time.append(minute)
                minute_bool = True

        if not second_bool:
            second = int(input('Enter second: '))
            if second < 0 or second > 59:
                print('Seconds must be between 0 and 59.')
                continue
            else:
                time.append(second)
                second_bool = True

    return time

def read_valid(unit, start, end):
    while True:
        number = int(input('Enter ' + unit + ': '))
        if number < start or end < number:
            print('ERROR: ' + str(unit) + ' must be between ' + str(start) + ' and ' + str(end))
            continue
        else:
            return number


def read_time():
    time = [] + [read_valid('hour', 0, 23)]
    time.append(read_valid('minute', 0, 59))
    time.append(read_valid('second', 0, 59))
    return time

# print(read_time())

def convert_time(time, mode):
    if mode == 'time':
        time_list = [] + [time // 3600]
        time_list.append((time - (time // 3600) * 3600) // 60)
        time_list.append(time % 60)
        return time_list
    elif mode == 'sec':
        seconds = 0
        for i in range(3):
            seconds += time[i] * 60 ** (2 - i)
        return seconds


# print(convert_time(8661, 'time'))

def travel_time():
    print('Give departure time in hour, minute and seconds:')
    departure = read_time()
    print()

    while True:
        print('Give arrival time in hour, minute and seconds:')
        arrival = read_time()

        if convert_time(departure, 'sec') > convert_time(arrival, 'sec'):
            print('ERROR: Arrival time must be later than departure time')
            continue
        else:
            break

    difference = convert_time(arrival, 'sec') - convert_time(departure, 'sec')
    difference = convert_time(difference, 'time')
    print('Traveltime:', difference[0], 'hours,', difference[1], 'minutes,', difference[2], 'seconds.')


# travel_time()

def bus_time(bus):
    return convert_time(bus[3:5] + [0], 'sec') - convert_time(bus[1:3] + [0], 'sec')


def analyze_bus_routes(bus_tables):
    # Initialise time initial time values
    fastest_time = slowest_time = bus_time(bus_tables[0])

    # Initialise the first bus index
    fastest_bus = slowest_bus = bus_tables[0][0]

    # Finds slowest bus
    for route in bus_tables:
        if bus_time(route) > slowest_time:
            slowest_time = bus_time(route)
            slowest_bus = route[0]

    # Find fastest bus
    for route in bus_tables:
        if bus_time(route) < fastest_time:
            fastest_time = bus_time(route)
            fastest_bus = route[0]

    # Get the times in list form
    slowest_list = convert_time(slowest_time, 'time')
    fastest_list = convert_time(fastest_time, 'time')

    # Print the results
    print('The slowest bus is', slowest_bus, 'and it takes', slowest_list[0], 'hours and', slowest_list[1], 'minutes')
    print('The fastest bus is', fastest_bus, 'and it takes', fastest_list[0], 'hours and', fastest_list[1], 'minutes')



busses = [[1, 15,  0, 15, 19],
          [3, 15, 32, 16, 45],
          [4, 15, 45, 16, 23],
          [5, 15, 55, 16, 11]]

analyze_bus_routes(busses)

