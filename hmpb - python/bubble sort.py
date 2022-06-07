# Implementation of bubble sort()

def bubleSort(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1) -i -1):
            if(list1[j] > list1[j+1]):
                aux = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = aux
    return list1

print(bubleSort([5,4,7,9,1,4,5,7,2]))
