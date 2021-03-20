def findMaxPoints(arr):
    if len(arr)<3:
        return arr[0]
    n=len(arr)
    
    sum_value=0
    for i in range(1,n+1,2):
        sum_arr=sum(arr[0:i])
        sum_value+=sum_arr
        for j in range(1,n-i+1):
            sum_arr=sum_arr-arr[j-1]+arr[j+i-1]
            sum_value+=sum_arr
    return sum_value
arr=[10, 3, 6, 5, 8, 6, 10, 9, 4, 4]
print(findMaxPoints(arr))