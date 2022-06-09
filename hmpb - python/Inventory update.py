import operator
# Inventory Update
'''Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery.
 Update the current existing inventory item quantities (in arr1). If an item cannot be found, add the new item and quantity into the inventory array. 
 The returned inventory array should be in alphabetical order by item.'''

def updateInventory(curInv, newInv):
    curInvDict = {item: count for count, item in curInv}
    newInvDict = {item: count for count, item in newInv}

    for key in newInvDict.keys():
        print(key)
        try:
            curInvDict[key] = curInvDict[key] + newInvDict[key]
        except KeyError:
            curInvDict[key] = newInvDict[key]
    updInv = []
    for item in sorted(curInvDict):
        aux = [curInvDict[item], item]
        updInv.append(aux)
    return(updInv)

# Example inventory lists
curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]
newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"],
]


print(updateInventory(curInv, newInv))
