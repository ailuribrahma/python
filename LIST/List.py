#List are used to store multiple items in single variable
#we have different values like numbers strings have to group then gther 
#assign multipule values using []
#List is mutable means it can be change value
#LIST items are ordered, changeable, and allow duplicate values
#List are one of 4 built in data types in Python other 3 are Tuple and set and Dictionary

#below examples assign numaric values to variable
print('this is number index')
nums = [70,20,30,50,40,60,10,90,10,10]
print(nums)

#below assign string values to variable
print('this is charecter index')
names = ['a','b','c','d','e','f']
print(names)

#assign difference type to one list it will work ex float value and string and int value to assign bellow
values = [9.5,'BRAHMA',10]
print(values)

#two lists working together 
 #mixList = [nums,names,values]
#print(mixList)

#this example is find value using index value
print(nums[4])

#if we want print some thing print between the values 
print(nums[3:])
print(nums[2:4])
print(nums[:5])
print(nums[0:2])
#we can use nagitive range as well
print(nums[-1])

#Append() insert element last of list 
print(nums.append(110))


#Insert() insert element anywhere If you want Ex: using index (0,1,2,3,4,5,6)
#print(nums.insert(0,100))

#Remove() remove value from list not based on index it’s remove actual value
#print(nums.remove(100))

#Pop() This will delete or remove value from list based on index
print(names.pop(2))
print(names)
print(nums.pop(2))

#delete values from the list using del commend
#del nums[1:]
#print(nums)
#del nums[:5]
#print(nums)
#del nums[3:8]
#print(nums)

#extend()
#add multiple values using predefind function below
nums.extend([110,120,130])
print(nums)

#min()
#find min value in list using min() predefind function
print('this is minmum value of nums list')
print(min(nums))

#max()
#find max value in list using max() predefind function
print(max(nums))
print(nums)

#sum()
#print sum of value in list using sum() function
print(sum(nums))
print(nums)

#sort()
#print sorted values using sort() function 
#nums.sort()
#print(nums)

#this operation using copy one list to other list
#copy()
#nums2 = nums.copy() 
#print(nums2)

#clear()
#nums.clear()
#print(nums)

#count()
#Return the number of times the value appears in the C list
#c = ['brahma','reddy','reddy','brahma','nani']
#print(c.count('reddy'))

#index()
#sytax: list.index(elmnt, start, end)
#print(nums.index(30))
#print(nums.index(10,4,9)) #(element,start,end)

#reverse()
#reverse is work below way to repregent only 
#nums.reverse()
#print(nums)

#find lenth of List
#len()
#print(len(nums))

#change value in index
#nums[3] = 100
#print(nums)

#change values using charecter index
#names[2:4] = ["ARJUN","BRAHMA"]
#print(names)
