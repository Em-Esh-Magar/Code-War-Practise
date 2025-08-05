import math as m
def is_prime(num):
    if num<=1:
        return False
    
    for i in range(2, int(m.sqrt(num))+1):
        if num%i == 0:
            return False
        
    return True

num = int(input("Enter a number : "))
print(is_prime(num))