def giveIceCream(n,k):
    if n<=k:
        return 1
    f=[1 for i in range(0,n+1)]
    f[0]=0
    f[1]=0
    
    for i in range(2,k+1):
        if f[i]==1:
            f[i]=0
            for j in range(2*i,n+1,i):
                f[j]=0
    s=0
    for i in range(2,n+1):
        s+=f[i]
    return s+1
n,k=map(int,input().split())
print(giveIceCream(n,k))
