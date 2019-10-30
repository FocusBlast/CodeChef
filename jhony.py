for _ in range(int(input())):
    a = int(input())
    play = list(map(int,input().split()))
    jhony = int(input())
    play1 = play.copy()
    play.sort()
    for i in range(len(play)):
        if(play[i] == play1[jhony-1]):
            b = i+1
    print(b)
