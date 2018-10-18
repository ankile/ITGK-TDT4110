def main():
    number = int(input('Enter a positive integer: '))

    min_sum = recursive_sum(number)

    print('The sum of the', number, 'first integers is', min_sum)

    numbers = [3, 6, 3, 6, 3, 1, 4, 3, 100, 124, 53, 2, 5, 223, 2, 234, 234, 234, 234, 234, 411]

    sorted_numbers = [] + numbers

    find_smallest_element(numbers)

    smallest_number = find_smallest_element(numbers)

    print('The smallest element in the list is', smallest_number)

    sorted_numbers.sort()

    print('sorted_numbers:', sorted_numbers)

    element = 3

    binary_search(sorted_numbers, element)

    index = binary_search(sorted_numbers, element)

    print(element, 'er på plass', index, 'i listen.')


def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n - 1)


def find_smallest_element(numbers):
    if len(numbers) == 1:
        # print(numbers[0])
        return numbers[0]
    elif numbers[len(numbers) - 1] > numbers[len(numbers) - 2]:
        numbers.remove(numbers[len(numbers) - 1])
    else:
        numbers.remove(numbers[len(numbers) - 2])

    # print('number:', numbers)
    find_smallest_element(numbers)


def binary_search(numbers, element):
    if len(numbers) == 1 and element != numbers[0]:
        return -float('inf')
    elif element == numbers[len(numbers) - 1]:
        return len(numbers) - 1
    else:
        numbers.pop()
        binary_search(numbers, element)

main()
