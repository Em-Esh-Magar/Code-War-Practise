def cipher(text):
    result = []
    for char in text:
        if 'a'<= char <='z':
            result.append(chr(((ord(char)-ord('a')+13) % 26) + ord('a')))
        elif 'A' <= char <='Z':
            result.append(chr(((ord(char)-ord('A')+13)%26)+ord('A')))
        else:
            result.append(char)
    
    return ''.join(result)
    
a = input("Enter a text : ")
encryption = cipher(a)
print(f"The encryption is {encryption}")

decryption = cipher(encryption)
print(f"The decryption is {decryption}")