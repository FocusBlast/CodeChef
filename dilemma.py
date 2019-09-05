test_case = int(input())
for i in range(test_case):
    enter_string = input()
    enter_string = list(enter_string)
    enter_string = list(map(int,enter_string))
    while(1 in enter_string):
        print(enter_string)
        for j in range(len(enter_string)):
            if(enter_string[j] == 1):
                enter_string[j] = "Null"
            if(j==0):
                if(enter_string[j-1]==0):
                    enter_string[j-1] = 1
                    flag = 0
                    for e in enter_string:
                        if(e != "Null"):
                            flag = 1
    print(enter_string)
    if flag == 0:
        print("LOSE")
    else:
        print("WIN")