# Rotation of a array/list by a key(shift by it)

def ListRotation(arr,key):
    array = arr.copy()
    
    for i in range(0,len(arr)):
        next = (i%len(arr))+key
        print(next)
        if next > len(arr)-1:
            next = next%len(arr)
            
        
        array[next] = arr[i]            
            
    return array


print(ListRotation([3,1,6,5,9],3))
