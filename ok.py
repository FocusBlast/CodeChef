for _ in range(int(input())):
    a = int(input())
    horses = list(map(int,input().split()))
    horses.sort()
    sub = 9999999999
    for i in range(1,len(horses)):
        if(horses[i]-horses[i-1]<sub):
            sub = horses[i]-horses[i-1]
    print(sub)
            
            
           
    
    
