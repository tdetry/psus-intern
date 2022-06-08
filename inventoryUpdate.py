"""

Inventory Update
Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery.
Update the current existing inventory item quantities (in arr1). If an item cannot be found, add the new item and quantity into the inventory array.
The returned inventory array should be in alphabetical order by item.

"""

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
    [7, "Toothpaste"]
]

def updateInv(currentInv, newInv):
    """
    Returns the updated inventory list.
    """
    updated_inventory = []
    # Loop through the newInv inventory.
    for newItem in newInv:
        bool_add = False
        # Loop through the CurrentInv inventory.
        for item in currentInv:
            # If the item in the current inventory is the same as the item in the new inventory,
            # add the quantity of the new item to the quantity of the current item.
            if item[1] == newItem[1]:
                bool_add = False
                item[0] += newItem[0]
                break
            else:
                bool_add = True
        #only add the item if it is not already in the current inventory.
        if bool_add: 
            updated_inventory.append(newItem)
                
    #join the current inventory and the updated inventory
    updated_inventory = updated_inventory + currentInv
    # Sort the updated inventory list by item.
    updated_inventory.sort(key=lambda x: x[1])
    return updated_inventory


updated_inventory = updateInv(curInv, newInv)
print(updated_inventory)
