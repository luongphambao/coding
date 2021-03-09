a,b= map(int, input().split())
if a>b:
    print(b)
else:
    s=b%(2*a)
    print(s%a-1)