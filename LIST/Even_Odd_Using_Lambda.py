#using Lambda function to find even and odd numbers in list
#using filter() function along with lambda function to filter even and odd numbers
numbers = [10, 23, 45, 66, 78, 91, 34, 22, 11, 9, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Even numbers in the list:", even_numbers)
print("Odd numbers in the list:", odd_numbers)  