def maxScore(cp, k):
    totalSum,subSum=sum(cp),sum(cp[:-k])
    ans=totalSum-subSum
    for i in range(k):
        subSum=subSum-cp[i]+cp[len(cp)-k+i]
        ans=max(ans,totalSum-subSum)
    return ans
cp=[1,2,3,4,5,6,1]
k = 3
print(maxScore(cp,k))