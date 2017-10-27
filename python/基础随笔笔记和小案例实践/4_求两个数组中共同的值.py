arr1 = [1,2,3,4,5,6,7,8,9,22,33,44,55]
arr2 = [2,4,5,8,3,33]
arr3 = []

for i in arr1:
    if i in arr2 and i not in arr3:
        arr3.append(i)
print arr3
