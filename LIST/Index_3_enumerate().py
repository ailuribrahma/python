# Using list comprehension with enumerate to find all indices of a specific element in a list
#if you neet to find all  indices an element appears, enumerate() combimed with list comprehension is and effective way to achieve this.

my_list = ['apple', 'banana', 'banana', 'banana', 'banana', 'grape']
all_indices = [i for i, item in enumerate(my_list) if item == 'banana']
print(f"All indices of are: {all_indices}")
# for item in enumerate(my_list):
#     print(item)

