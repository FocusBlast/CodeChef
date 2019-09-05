t=int(input())
for i in range(t):
    n=int(input())
    c=[int(x)for x in input().split()]
    print(c)
    h=[int(x)for x in input().split()]
    print(h)
    s=0
    for i in range(n):
        low=(i+1)-c[i]
        high=(i+1)+c[i]
        if(low<0):
            low=0
        if(high>=n):
            high=n
            print(high)
        if(low==0):
            s+=(high-low)
        else:
            s+=(high-low)+1
    if(s==sum(h)):
        print("YES")
    else:
        print("NO")
    