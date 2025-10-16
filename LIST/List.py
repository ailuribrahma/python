#List are used to store multiple items in single variable
#we have different values like numbers strings have to group then gther 
#assign multipule values using []
#List is mutable means it can be change value
#LIST items are ordered, changeable, and allow duplicate values
#List are one of 4 built in data types in Python other 3 are Tuple and set and Dictionary

#below examples assign numaric values to variable
#print('this is number index')
#nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#print(nums)

#below assign string values to variable
#print('this is charecter index')
#names = ['a','b','c','d','e','f']
#print(names)

#assign difference type to one list it will work ex float value and string and int value to assign bellow
#values = [9.5,'BRAHMA',10]
#print(values)

#two lists working together 
#mixList = [values, nums, names]
#print(*mixList, sep='\n')

#this example is find value using index value
#print(nums[4])

#if we want print some thing print between the values 
#print(nums)
#print(nums[3:])
#print(nums[2:4])
#print(nums[:5])
#print(nums[0:2])
#we can use nagitive range as well
#print(nums[-1])

#Append() insert element last of list 
#print(nums.append(110))


#Insert() insert element anywhere If you want Ex: using index (0,1,2,3,4,5,6)
#print(nums.insert(0,100))

#Remove() remove value from list not based on index it’s remove actual value
#print(nums.remove(100))

#Pop() This will delete or remove value from list based on index
#print(names.pop(2))
#print(names)
#print(nums.pop(2))

#delete values from the list using del commend
#del nums[1:]
#print(nums)
#del nums[:5]
#print(nums)
#del nums[3:8]
#print(nums)

#extend()
#add multiple values using predefind function below
#nums.extend([110,120,130])
#print(nums)

#min()
#find min value in list using min() predefind function
#print('this is minmum value of nums list')
#print(min(nums))

#max()
#find max value in list using max() predefind function
#print(max(nums))
#print(nums)

#sum()
#print sum of value in list using sum() function
#print(sum(nums))
#print(nums)

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




#-------------------------------------------------------------------------------------------------------
                                           
                                     #interview questions on list
#--------------------------------------------------------------------------------------------------------
                             #How to take input from user and store in list?
                             #refer LIST/input()method programs
#--------------------------------------------------------------------------------------------------------
                                      #How to reverse a list
                                #refer LIST/reverse()method programs
#--------------------------------------------------------------------------------------------------------
                #How to display list values using user given starting and ending index values
                           #refer LIST/DisplayValuesStartingEndingIndex.py 
#--------------------------------------------------------------------------------------------------------
                


#How to find sum of list values
#How to find largest and smallest number in list
#How to remove duplicates from list
#How to sort list values in ascending and descending order
#How to find second largest number in list
#How to find second smallest number in list
#How to find even and odd numbers in list
#How to find common elements from two lists
#How to find missing numbers in list
#How to copy one list to another list
#How to find index of an element in list
#How to check if an element exists in list
#How to concatenate two lists
#How to find length of list
#How to clear all elements from list
#How to iterate through a list
#How to create a list of lists (2D list)
#How to flatten a list of lists
#How to find all permutations of a list
#How to find all combinations of a list
#How to find the intersection of two lists
#How to find the union of two lists
#How to find the difference between two lists
#How to find the symmetric difference between two lists
#How to find the frequency of elements in a list
#How to sort a list of tuples based on a specific element
#How to group elements of a list based on a specific condition
#How to find the median of a list of numbers
#How to find the mode of a list of numbers
#How to find the range of a list of numbers
#How to find the variance of a list of numbers
#How to find the standard deviation of a list of numbers
#How to find the cumulative sum of a list of numbers
#How to find the moving average of a list of numbers
#How to find the z-score of a list of numbers
#How to find the percentile of a list of numbers
#How to find the quartiles of a list of numbers
#How to find the interquartile range of a list of numbers
#How to find the skewness of a list of numbers
#How to find the kurtosis of a list of numbers
#How to find the correlation between two lists of numbers
#How to find the covariance between two lists of numbers
#How to find the linear regression line for a list of numbers
#How to find the polynomial regression line for a list of numbers
#How to find the exponential regression line for a list of numbers
#How to find the logarithmic regression line for a list of numbers
#How to find the power regression line for a list of numbers
#How to find the moving median of a list of numbers
#How to find the moving mode of a list of numbers
#How to find the moving range of a list of numbers
#How to find the moving variance of a list of numbers
#How to find the moving standard deviation of a list of numbers
#How to find the moving z-score of a list of numbers
#How to find the moving percentile of a list of numbers
#How to find the moving quartiles of a list of numbers
#How to find the moving interquartile range of a list of numbers
#How to find the moving skewness of a list of numbers
#How to find the moving kurtosis of a list of numbers
#How to find the moving correlation between two lists of numbers
#How to find the moving covariance between two lists of numbers
#How to find the moving linear regression line for a list of numbers
#How to find the moving polynomial regression line for a list of numbers
#How to find the moving exponential regression line for a list of numbers
#How to find the moving logarithmic regression line for a list of numbers
#How to find the moving power regression line for a list of numbers
#How to find the cumulative product of a list of numbers
#How to find the cumulative maximum of a list of numbers
#How to find the cumulative minimum of a list of numbers
#How to find the cumulative count of a list of numbers
#How to find the cumulative frequency of a list of numbers
#How to find the cumulative distribution function of a list of numbers
#How to find the probability density function of a list of numbers
#How to find the histogram of a list of numbers
#How to find the box plot of a list of numbers
#How to find the scatter plot of two lists of numbers
#How to find the line plot of a list of numbers
#How to find the bar plot of a list of numbers
#How to find the pie chart of a list of numbers
#How to find the heatmap of a list of numbers
#How to find the violin plot of a list of numbers
#How to find the swarm plot of a list of numbers
#How to find the pair plot of a list of numbers
#How to find the joint plot of two lists of numbers
#How to find the regression plot of two lists of numbers
#How to find the residual plot of two lists of numbers
#How to find the autocorrelation of a list of numbers
#How to find the partial autocorrelation of a list of numbers
#How to find the seasonality of a list of numbers
#How to find the trend of a list of numbers     