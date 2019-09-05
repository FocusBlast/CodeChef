test_case = int(input())
for i in range(test_case):
    enter_string = input()
    enter_string = list(enter_string)
    if enter_string.count('1')%2 ==0:
        print("LOSE")
    else:
        print("WIN")