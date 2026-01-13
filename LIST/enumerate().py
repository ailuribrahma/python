#Python’s enumerate() function helps you with loops that require a counter by adding 
# an index to each item in an iterable. This is particularly useful when you need both 
# the index and value while iterating, such as listing items with their positions. 
# You can also customize the starting index with the start argument, offering 
# flexibility in various scenarios.

#without enumerate()
fruits = ['apple', 'banana', 'cherry', 'lychee', 'mango', 'orange']
vegitables = ['carrot', 'broccoli', 'spinach']  
i=0
for item_1 in fruits:
        print(f"{i}  {item_1}")
        i+=1

#with enumerate()
fruits = ['apple', 'banana', 'cherry', 'lychee', 'mango', 'orange']
for index, item_1 in enumerate(fruits):
        print(f"{index}  {item_1}") 