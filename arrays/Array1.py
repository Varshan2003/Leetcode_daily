#reverse an array

def reverseAnArray(arr,s,e):
    start = s
    end=e
    while start<end:
            arr[start],arr[end] = arr[end],arr[start]
            end-=1
            start+=1
    return arr
print(reverseAnArray([1,2,3,4],0,3))