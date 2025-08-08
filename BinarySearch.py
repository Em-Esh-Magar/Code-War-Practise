def BinarySearch(arr,key):
    index = -1
    arr.sort()
    mid = l = 0
    h = len(arr)-1
    
    while (l<=h):
        mid = int((l+h)/2)
        
        if arr[mid]==key:
            index = mid
            break
        
        elif arr[mid]<key:
            l = mid+1
            
        else:
            h = mid - 1
    
    return index

index = BinarySearch([8,1,4,2,6,7,9,5],9)
if index == -1:
    print("Doesn't found")
    
else:
    print(f"Found in {index}th index")

