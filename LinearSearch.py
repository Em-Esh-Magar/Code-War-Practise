
def LinearSearch(arr,key):
    index = -1
    for i in range(0,len(arr)):
        if key == arr[i]:
            index = i
            break
    
    return index

index = LinearSearch([8,1,4,2,6,7,9,5],9)
if index == -1:
    print("Doesn't found")
    
else:
    print(f"Found in {index}th index")

