no_of_times = int(input())
for i in range(no_of_times):
    l = str(input())
    count = 0
    for elem in l:
        if(elem == '4'):
            count +=1
    print(count)