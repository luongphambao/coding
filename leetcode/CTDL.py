from sys import stdin
def binarySearch(arr,left,right,x):
    if arr[right]<=x:
        return right
    if arr[left]>x:
        return left
    mid=(left+right)//2 
    if (arr[mid] <= x and arr[mid + 1] >= x) : 
        return mid  
    
    if(arr[mid] < x) : 
        return binarySearch(arr, mid + 1, right, x) 
      
    return binarySearch(arr,left, mid - 1, x)

def printKclosest(arr, x, k, n) : 
    if arr[0]>=x:
        return str(arr[0])+" "+str(arr[k-1])
    if arr[-1]<=x:
        s=arr[-k:]
        return str(s[0])+" "+str(s[-1])
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
  
    return (str(arr[l+1])+" "+str(arr[r-1]))
n = int(stdin.readline())
arr = [int(i) for i in stdin.readline().split()]
a=[1]
while (a!=[]):
    a = [int(i) for i in stdin.readline().split()]
    if a == []:
        break
    k, x = a[0], a[1]
    print(printKclosest(arr,x,k,n))
    
a='12334\n'
print()