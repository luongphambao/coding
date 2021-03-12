from sys import stdin

sta = set()
while True:
    x = [int(i) for i in stdin.readline().split()]
    if len(x) == 0:
        continue
    a=x[0]
    if a == 0:
        break
    elif a == 1:
        sta.add(x[1])
    elif a == 2:
        print(int(x[1] in sta))
    else:
        if x[1] in sta: 
            sta.remove(x[1])
        else:
            continue