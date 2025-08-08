import string

def Panagram(Str):
    return set(string.ascii_lowercase) <= set(str.lower())

str = input("Enter a sentences : ");
print(Panagram(str))