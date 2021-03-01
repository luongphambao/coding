n=int(input())
def fibo(n):
    if n<=0 or n>30:
        return -1 
    f=[1 for i in range(n)] 
    if n<=2:
        return 1
    for i in range(2,n):
        f[i]=f[i-1]+f[i-2]
    return f[n-1]
s=fibo(n)
if s==-1:
    print(f'So {n} khong nam trong khoang [1,30].')
else:
    print(s)