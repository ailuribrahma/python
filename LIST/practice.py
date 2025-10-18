list = [10, 20, 30, 40, 50]
print("The original list is:", list)
for i in list:
    print(i)
    if i == 30:
        break
    print("Inside the loop")
print("Exit")
