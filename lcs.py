def getThePassword(key1,key2):
    m=len(key1)
    n=len(key2)
    L = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0 #base case
            elif key1[i-1]==key2[j-1]:
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i][j-1],L[i-1][j])
    if L[m][n]==0:
        return 6008009
key1='aaMMumMaaF"'
key2='hOcOOiIKr '
print(getThePassword(key1,key2))