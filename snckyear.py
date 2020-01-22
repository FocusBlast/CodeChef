lst = [2010, 2015, 2016, 2017, 2019]
for _ in range(int(input())):
    year = int(input())
    if year in lst:
        print("HOSTED")
    else:
        print("NOT HOSTED")
