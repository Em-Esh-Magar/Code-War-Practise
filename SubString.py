def Substring(array):
    
    substring = []
    
    for i in range(0,len(array)):
        
        for j in range(i+1,len(array)+1):
            substring.append(array[i:j])
            
    print(substring)
    
Substring([1,2,3,4,5])