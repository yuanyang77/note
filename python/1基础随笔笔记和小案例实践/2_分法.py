arr = [1,2,5,3,8,9,100,576,19999,32458,30000,200,3000]
num_to_find = 7
start = 0
end = len(arr)-1
count = 0

while True:
    count += 1
    mid = (start+end)/2
    mid_num = arr[mid]
    if mid == start:
        print 'can not find ,should after %s=>%s'%(start,arr[start])
        break

    if num_to_find<mid_num :
        end = mid
    elif num_to_find>mid_num:
        start = mid
    else:
        print 'find',mid
        break
print count
