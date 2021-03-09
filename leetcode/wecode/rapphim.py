a,b,c=map(int, input().split())
s1,s2=a//c,b//c
if a%c!=0: 
    s1+=1
if b%c!=0:
    s2+=1 
print(s1*s2) 