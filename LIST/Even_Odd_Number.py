numbers = [10, 23, 45, 66, 78, 91, 34, 22, 11, 9, 8]
even_numbers = []
odd_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print("Even numbers in the list:", even_numbers)
print("Odd numbers in the list:", odd_numbers)