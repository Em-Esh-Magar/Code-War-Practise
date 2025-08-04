
def Anagram(word1, word2):
    
    if " " in word1:
        word1 = word1.replace(" ","")
        print(word1)
        
    if " " in word2:
        word2 = word2.replace(" ","")
        
    return sorted(word1.lower()) == sorted(word2.lower()) 
    
        
        
print(Anagram("L is ten","Silent"))