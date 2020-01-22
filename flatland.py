# cook your dish here
import math

t = int(input())

while t>0:
    
    n = int(input())
    c=0
    while n>0:
        
        x = int(math.sqrt(n))
        n-=(x*x)
        
        c+=1

    print(c)
    t-=1
