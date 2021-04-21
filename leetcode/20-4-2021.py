s = input()
m = len(str(s))
d=0
flag=0
for i in range(m):
    d+=int(s[i])
d %= 3
d1 = 3 - d
for i in range(m):
    if int(s[i])+d1<=9:
        flag=1
        while int(s[i])+d1<=9:
            s[i]=str(int(s[i])-d)
            d1=3
            break
    if flag==0:
        for i in range(m-1, 0, -1):
            if int(s[i])-d>=0:
                s[i]=str(int(s[i])-d)
            break
print(s)