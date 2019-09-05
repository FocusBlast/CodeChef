k = int(input())
for i in range(k):
    size = int(input())
    arr = input().split()
    arr = list(map(int, arr))
    for i in range(len(arr)-1):
        mul = arr[i]*arr[i+1]
    if mul in arr:
        print("yes")
    else:
        print("no")
    