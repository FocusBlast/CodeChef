arr = [1,2,3,4,5]
n = [0,0,0,0,0,0,0]
for i in range(len(n)+2):
    n = i-arr[i]+1
    print(n)
    #print(b)