ans = []
sta = set()
mission = []
while True:
    x = [int(i) for i in input().split()]
    if x[0] == 0:
        break
    elif x[0] == 1:
        sta.add(x[1])
    else:
        if x[1] not in sta:
            ans.append(0)
        else:
            ans.append(1)
for i in ans:
    print(i, end = "\n")