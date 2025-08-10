def missingNumbers(arr, brr):
    # Write your code here
    missing = []
    
    empty = set() 
    for i in brr:
        empty.add(i)
    
    # print(empty)
    for i in empty:
        print(i)
        if arr.count(i) == brr.count(i):    
            print("hello")        
        
        else:
            missing.append(i)
        
    missing.sort()
    print(missing)
    return missing

print(missingNumbers([203,204,205,206,207,208,203,204,205,206],[203,204,204,205,206,207,205,208,203,206,205,206,204,210]))