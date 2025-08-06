
def Substring(array):
    substring = []
    
    for i in range(0, len(array)):
        for j in range(i+1,len(array)+1):
            
            substring.append(array[i:j])
            
    return substring


def Highest_SubString(array):
    highest = 0
    sum = 0
    for items in array:
        for x in items:
            sum +=x
            
            if sum > highest:
                highest = sum
                
        sum = 0
        
    return highest


substring = Substring([1,2,3,4,5,6])
highest = Highest_SubString(substring)
print(highest)