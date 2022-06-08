#Write a Python program to convert a tuple to a string.

from click import option


mytuple = ("h", 'o','l', 'a', ' ', 'm', 'u', 'n', 'd', 'o')
output = ''
print(output.join(mytuple))

#Write a program to unpack the 
#following tuple into four variables and display each variable.

tuple1 = (10, 20, 30, 40)
val1, val2,val3, val4 = tuple1[0:4]
print(val1, val2, val3, val4)
numbers = []


def frecuency_times(list):
    new_list = []
    for n in list:
      if  (n, list.count(n)) not in new_list:
          new_list.append((n, list.count(n)))
    return new_list
          
        
    
print(numbers)
print("select an option")
print("1 add number")
print("2 delete number")
print("3 Show list")
print("4 Add all numbers")
print("5 filter numbers below n")
print("5 filter numbers below n")
print("6 Frecuency")



print("0 End")

user_option = int(input("Option: "))

while user_option != 0:
    
    if user_option == 1:
        print("Insert a number")
        num = int(input("Number: "))
        while num != 0:
            numbers.append(num)  
            num = int(input("Number 0 to end: "))
        print(numbers)
    if user_option == 2:
        print("Insert number to delete")
        num = int(input("Number: "))
        if num in numbers:   
            numbers.remove(num)
            print("numero eliminado")
        else:
            print("numerono existe")
    if user_option == 3:
        print(numbers)
    if user_option == 4:
        total = 0
        for item in numbers:
            total += item
        print(total)
    if user_option == 5:
        limit = int(input("limit number: "))
        filter_list = []
        for item in numbers:
            if item < limit:
                filter_list.append(item)
        print(filter_list)                
    if user_option == 6:
        for tupla in frecuency_times(numbers):
            print(tupla[0], "is", tupla[1], "times")
            
 
    print("select an option")
    print("1 add number")
    print("2 delete number")
    print("3 Show list")
    print("4 Add all numbers")
    print("5 filter numbers below n")
    print("6 Frecuency")
    print("0 End")

    user_option = int(input("Option: "))