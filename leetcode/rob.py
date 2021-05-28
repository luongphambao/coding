def rob(arr):
    F=[0]*len(arr)
    if len(arr)<=2:
        return max(arr)
    F[0]=arr[0]
    F[1]=max(arr[0],arr[1])
    for i in range(2,len(arr)):
        F[i]=max(F[i-2]+arr[i],F[i-1])
    return F[len(arr)-1]
arr=[2,1,1,2]
print(rob(arr))