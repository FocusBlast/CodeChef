test = int(input())
for i in range(test):
    players = int(input())
    goals = []
    fouls = []
    goals = map(int,input().split())
    fouls = map(int,input().split())
    raw_score = [0]
    for k,l in zip(goals, fouls):
        raw_score.append((k*20)-(l*10))
    print(max(raw_score))