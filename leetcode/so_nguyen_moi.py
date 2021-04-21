from sys import stdin, stdout
n = stdin.readline().strip()

sodu = 3 - int(n) + int(n)//3*3
l = len(n)
ck = 0
m = int(n)

for i in range(l):
    if m//10**(l-i-1)%10+sodu<10:
        m = m + sodu*10**(l-i-1)
        ck = 1

    while(ck==1 and m//10**(l-i-1)%10+3<10):
        m = m + 3*10**(l-i-1)
        
    if ck ==1:
        break

    if m%3!=0 and i == l-1:
        x=m%3
        m = m - x
        break

    if m%3==0 and i==l-1:
        m=m-3 

print(m)