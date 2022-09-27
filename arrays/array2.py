def MaxAndMin(arr):
    start = 0
    arr.sort()
    return "the max is "+str(arr[0])+ " the min is "+str(arr[-1])

print(MaxAndMin([1,2,3,9,4]))