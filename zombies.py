test_cases=int(input())
for a in range(test_cases):
    no_of_elements = int(input())
    radiation_caves = [int(x)for x in input().split()]
    health_of_zombies = [int(x)for x in input().split()]
    final = 0
    for a in range(no_of_elements):
        down = (a+1)-radiation_caves[a]
        up = (a+1)+radiation_caves[a]
        if(down < 0):
            down = 0
        elif(up >= no_of_elements):
            up = no_of_elements
        elif(down == 0):
            final += (up-down)
        else:
            final += (up-down) + 1   
    if(final == sum(health_of_zombies)):
        print("Yes")
    else:
        print("No")
    
    