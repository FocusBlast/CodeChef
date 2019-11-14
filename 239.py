t = int(input())
while(t):
    l,r = map(int,input().split())
    l_d = 0
    c = 0 
    for i in range(l,r+1):
        l_d = i % 10 
        if(l_d == 2 or l_d == 3 or l_d == 9):
            c += 1 
    print(c)
    t -= 1