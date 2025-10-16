my_list = [10, 10, 30, 30, 20, 40, 50, 50]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)        
        print("List without duplicates:", unique_list)