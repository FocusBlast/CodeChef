test_cases = int(input())
for i in range(test_cases):
    apples_boi = input().split()
    apples_boi = list(map(int, apples_boi))
    print(apples_boi)
for j in range(len(apples_boi)-1):
    if((apples_boi[j]%apples_boi[j-1])//len(apples_boi) == 0):
        print("Yes")
    else:
        print("No")

