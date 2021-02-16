def maxAbsSum(arr):
    s=0
    arr.sort()
    item=[]
    for i in range(len(arr)//2):
        item.append(arr[i])
        item.append(arr[len(arr)-1-i])
    if len(arr)%2!=0:item.append(arr[len(arr)//2])
    item.append(item[0])
    for j in range(1,len(item)):
        s+=(abs(item[j]-item[j-1]))
    return s
