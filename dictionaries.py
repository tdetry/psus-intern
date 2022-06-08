# Initializing a dictionary
store = {}

# Filling the dictionary with random values
for i in range(5):
    store[i] = i*3

print("The dictionary looks like this initially: ", store)

# Printing all the keys from the dictionary
print("Printing all the keys: ", store.keys())

# Printing all the values from the dictionary
print("Printing all the values: ", store.values())

# Add key-value pair to the dictionary
store[10] = 10*3
print("Appending an element to the dictionary", store)

# Delete a key from the dictionary
del store[2]
print("Removing a key using del", store)

store.pop(0)
print("Deleting a key using pop", store)

store.popitem()
print("Deleting the last entered item", store)

# Check if a key exists in the dictionary
if 3 in store:
    print("key 3 is in the dictionary: 3 => ", store[3])
else:
    print("key 3 not found")

# Checking if a key exists using try except
try:
    print("Key found: ", store[3])
except:
    print("Key not found")

# Merge dictionaries
dict2 = {0:0, 2: 99, 99:3}
print("Appending and updating a new dictionary to the original one: ", store.update(dict2))

