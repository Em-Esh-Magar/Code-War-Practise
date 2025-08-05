a = [0,1]

for i in range (0,15):
    n1 = len(a)-1
    n2 = len(a)-2
    
    a.append(a[n1]+a[n2])
    
print(a)