#Dictinary repersent key value pairs
#we can fatch data from key and key is unic

#Data = {1:'AAA',2:'BBB',3:'CCC',4:'DDD',5:'EEE'}

#print(Data.get(1))
#print(Data.get(2))

#if you merge keys values from data like below using dict(zip()) function below

#keys = [1,2,3,4]
#values = ['java','c#','python','.Net']
#Data = dict(zip(keys,values))
#print(Data)

#add data to dictionary

#Data[5] = 'Angular'
#print(Data)

#del data to dictionary

#del Data[4]
#print(Data)


#advance Technics for pricatice perpose
Data = {'JS':'Atom','CS':'VS','Python':['Pycharm','Sublime'],'java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(Data['java']['JSE'])