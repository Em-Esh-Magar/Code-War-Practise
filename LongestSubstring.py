def Substring(string):
    substring = []
    for i in range (0, len(string)):
        for j in range(i+1, len(string)+1):
            substring.append(string[i:j])
            
    return substring


def LongestSubString(substring):
    substring = sorted(substring,key = len)
    print(substring)
    return substring[-1]

substring = Substring("hello")
print(substring)
print(LongestSubString(substring))