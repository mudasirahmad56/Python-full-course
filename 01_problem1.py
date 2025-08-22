a = 1
b = 15
c = 12

def greater(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
a = 1
b = 15
c = 12
print(greater(a,b,c))

