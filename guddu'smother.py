for _ in range(int(input())):
    no_of_elements = int(input())
    numbers = [int(x)for x in input().split()]
    count = 0
    xor = []
    for i in range(len(numbers)-1):
        value = numbers[i]^ numbers[i+1]
        print(value)
        xor = xor + [value]
print(xor)
 