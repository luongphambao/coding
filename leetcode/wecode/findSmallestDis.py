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
    if (arr[l] == x) : 
        l -= 1
    while (l >= 0 and r < n and count < k) : 
          
        if (x - arr[l] < arr[r] - x) : 
            print(arr[l], end = " ")  
            l -= 1
        else : 
            print(arr[r], end = " ")  
            r += 1
        count += 1
  
    while (count < k and l >= 0) : 
        print(arr[l], end = " ") 
        l -= 1
        count += 1 
    while (count < k and r < n) :  
        print(arr[r], end = " ") 
        r += 1
        count += 1
printKclosest(arr,x,k,n)