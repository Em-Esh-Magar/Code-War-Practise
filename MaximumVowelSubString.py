# find the maximum number of vowels letters from sub array of string(which must be k length)

def MaximumVowels(str, k):
    subarray = []
    
    for i in range(0,len(str)):
        for j in range(i+1,len(str)+1):
            subarray.append(str[i:j])
           
    count = maximum = 0 
    for items in subarray:
        if len(items) == k:
            for i in items:
                if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                    count+=1
        
        if maximum < count :
            maximum = count
        
        count = 0
        
    return maximum

print(MaximumVowels("leetcode",4))