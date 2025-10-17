#set is collection of unicelements

#represention of set below like
#print secuence order  is not posible, there is no ascending and descending order print random values because set using concept of HASH
#using HASH perfomace is so fast  
#we want speed not need to secuence 
#index is not working because there is no secuence 



numbers = []
while True:
    user_input = input("Enter a number")
    if user_input.lower() == 'done':
        break
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("The list of numbers is:", numbers)