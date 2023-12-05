numbers = [10, 5, 8, 20, 15]

smallest_number = numbers[0]

for number in numbers:
    if number < smallest_number:
        smallest_number = number

print(f"The smallest number in the list is: {smallest_number}")
