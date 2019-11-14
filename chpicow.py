def animals(chickens, pigs, cows):
    chlegs = 2
    cowlegs = 4
    piglegs = 4
    print(chlegs*chickens + cowlegs*cows + piglegs*pigs)
chickens, pigs, cows = list(map(int, input().split()))
animals(chickens, pigs, cows)