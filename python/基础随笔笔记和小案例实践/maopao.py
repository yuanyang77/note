arr = [111,43,2,99,31,0,88,576,7]
count = 0
for j in arr:
   for i in range(len(arr)-1):
     count +=1
     if arr[i]>arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
   print arr
print count
print arr
