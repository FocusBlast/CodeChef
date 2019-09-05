arr = []
#The number of test cases
test_cases = int(input())
#entering the numbers
for _ in range(test_cases):
    #splitting the string and then converting them to integers and appending them.
    arr = str(input()).split()
    arr = map(int,  arr)
    print(arr)