ha = {'0':6, '1':2, '2':5, '3':5, '4':4, '5':5, '6':6,'7':3, '8':7,'9':6}
for _ in range(int(input())):
    a,b = [int(x) for x in input().split()]
    s = str(a+b)
    su = 0
    for i in s:
        su+=ha[i]
    print(su)
