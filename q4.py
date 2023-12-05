numbers = [10, 5, 8, 20, 15]

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number

print(f"The largest number in the list is: {largest_number}")
