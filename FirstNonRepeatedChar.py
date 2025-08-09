# The first non repeated character in string (case insensitive)
def FirstNonRepeated(str):
    count = ''
    for i in str:
        if str.count(i) == 1:
            count = i
            break
            
    return i 
        

str = input("Enter a string : ")
print(f"The First Non Repeated chareacter is : {FirstNonRepeated(str.lower())}")