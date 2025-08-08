def Panagram(str):
    count = set()
    for char in str.lower():
        if 'a' <= char <='z':
            count.add(char)
            
    if len(count) == 26:
        return True
    else:
        return False

str = input("Enter a sentences : ");
print(Panagram(str))