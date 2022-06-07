
####List excercises###
list1 = list(range(1,9))
# calculate the square of each element in a list
list2 = [num*num for num in list1]
print(list2)

#reverse the list
list2.reverse()
print(list2)

#copy the list and delete the second element
copy =list2.copy()
copy.pop(1)
print(copy)
print(list2)

#add the first list with the copy
list1.extend(copy)
print(list1)

#print the evens of the list
for num in list1:
    if(num%2 == 0):
        print(num)
 

#######tuples excercises########
#convert list1 into a tuple
tuple1 = tuple(list1)
print(tuple1)

a, *b, c = tuple1
print(a)
print(c) 
print(b)

#######dictionaries excercises########
dict1 = {"name": "hector", "age": 23, "city": "Mexico"}
#print the age
print(dict1["age"])

#change age to 20
dict1["age"] = 20
print(dict1["age"])

#print all the keys in dict1
for key in dict1.keys():
    print(key)

#print all the keys and values un dict1
for key, value in dict1.items():
    print(key, value)

dict2 = dict(lastName="Perez", tetragram="hmpb", city="polanco")

#update dict1 with dict2
dict1.update(dict2)
print(dict1)

