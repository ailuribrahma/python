list1 = [1,2,3,4,5]
list2 = [4,5,8,9,10]

#using set intersection
intersection = list(set(list1) & set(list2))
intersection_list = list(intersection)
print(intersection_list)

#using lambda and filter
intersection = list(filter(lambda x: x in list1, list2))
print(intersection)
