# Lists
nums = [1, 2, 8, 4, 5, 6]
print("The Original list", nums)

# Deep copy
dummy = nums[:]
print("Deep copy = ", dummy)

# Slice
sliced = nums[2:]
print("sliced = ", sliced)

# Reverse
reversedList = nums[::-1]
print("reversed list = ", reversedList)

# Sort
nums.sort()
print("Sorted list using .sort()", nums)

sorted(nums, key=lambda x: x)
print("Sorted list using sorted() and a lambda function = ", nums)

# Add an element at the end of the list
nums.append(10)
print("Adding 10 at the end of the list: ", nums)

# Add an element at a given index
nums.insert(3, 12)
print("Inserting 12 at the 3rd index: ", nums)

# Removing an element at a given index
nums.pop(0)
print("Removed the first element: ", nums)

nums.pop()
print("Removed the last element: ", nums)

# Adding a list to another list
nums.extend([11, 12, 13, 14, 15])
print("Appending a list upon another: ", nums)

# One line for loop on lists
squares = [i*i for i in nums]
print("Squaring every element in the nums list: ", squares)