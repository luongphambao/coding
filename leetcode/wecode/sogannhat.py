n=int(input())
arr = list(map(int,input().strip().split()))[:n]
k,x=map(int,input().strip().split())
def binarySearch(arr,left,right,x):
    if arr[right]<=x:
        return right
    if arr[left]>x:
        return left
    mid=(left+right)//2 
    if (arr[mid] <= x and arr[mid + 1] > x) : 
        return mid  
    
    if(arr[mid] < x) : 
        return binarySearch(arr, mid + 1, right, x) 
      
    return binarySearch(arr,left, mid - 1, x)

def printKclosest(arr, x, k, n) : 
      
    l = binarySearch(arr, 0, n - 1, x) 
    r = l + 1 
    count = 0
    a=[]
    b=[]
    if (arr[l] == x) :
        a.append(x) 
        count+=1
        l -= 1
    while (l >= 0 and r < n and count < k) : 
          
        if (x - arr[l] <= arr[r] - x) : 
            a.append(arr[l])  
            l -= 1
        else : 
            b.append(arr[r])   
            r += 1
        count += 1
  
    while (count < k and l >= 0) : 
        a.append(arr[l])  
        l -= 1
        count += 1 
    while (count < k and r < n) :  
        b.append(arr[r])  
        r += 1
        count += 1
    c=a[::-1]+b 
    print(*c)
printKclosest(arr,x,k,n)