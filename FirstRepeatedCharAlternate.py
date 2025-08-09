# The first repeated character in string (case insensitive) Alternate version
def FirstRepeated(str):
    count = ''
    emptyset = set()
    for i in str:
        if i in emptyset:
            count = i
            break
        
        emptyset.add(i)
            
    print(len(emptyset))
    print(emptyset)
    return i 
        

str = input("Enter a string : ")
str = str.replace(" ","")
print(str)
print(f"The First Repeated character is : {FirstRepeated(str.lower())}")