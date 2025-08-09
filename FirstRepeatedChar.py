# The first repeated character in string (case insensitive)
def FirstRepeated(str):
    count = ''
    for i in str:
        if str.count(i) != 1:
            count = i
            break
            
    return i 
        

str = input("Enter a string : ")
print(f"The First Repeated chareacter is : {FirstRepeated(str.lower())}")