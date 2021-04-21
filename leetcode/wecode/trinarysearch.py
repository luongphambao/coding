def TrinarySearch(arr, left, right, x, dem, arr1):
    if left <= right:
        i = (right +2*left) // 3
        j = (right*2 + left) // 3+1
        if x == arr[i]:
            arr1.append(dem)
            return i
        if x == arr[j]:
            arr1.append(dem)
            return j
        if x < arr[i]:
            return TrinarySearch(arr, left, i - 1, x, dem + 1, arr1)
        elif x > arr[j]:
            return TrinarySearch(arr, j + 1, right, x, dem + 1, arr1)
        else:
            return TrinarySearch(arr, i + 1, j - 1, x, dem + 1, arr1)
    arr1.append(dem)
    return -1

x = int(input())
arr = list(map(int, input().strip().split()))[:x]
n = int(input())
arr1 = list(map(int, input().strip().split()))[:n]
arr2 = []
for i in range(0, n):
    dem = 0
    index = TrinarySearch(arr, 0, x - 1, arr1[i], dem + 1, arr2)
    print(index,arr2[i])