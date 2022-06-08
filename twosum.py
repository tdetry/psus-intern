def twoSum(arr, target):
    subTargets = {}
    for index in range(len(arr)):
        curr = arr[index]
        if curr in subTargets:
            return [subTargets[curr], index]
        else:
            currDiff = target - curr
            subTargets[currDiff] = index
    return []

arr1 = [6, 3, 4];
target1 = 10;

arr2 = [3, 5, 2, 7, 4, 5];
target2 = 12;

arr3 = [3, 6, 2, 9];
target3 = 100;

arr4 = [];
target4 = 0;

print(twoSum(arr1, target1))
print(twoSum(arr2, target2))
print(twoSum(arr3, target3))
print(twoSum(arr4, target4))