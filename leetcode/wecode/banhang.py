n=int(input())
def EqualStr(s1,s2):
    for i in range(len(s1)):
        if s1[i] in s2: return "YES"
    return "NO"
for i in range(n):
    a=str(input())
    b=str(input())
    print(EqualStr(a,b))
