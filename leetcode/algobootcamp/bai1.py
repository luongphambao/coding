from sys import stdin
def maxSubSum(matrix, subLength):
    minSum = 10**9+7;

    for firstRow in range(0,len(matrix)-subLength+1):
        for firstCol in range(0,len(matrix[0])-subLength+1):
            sum_value = 0
            for row in range(3):
                for col in range(3):
                    sum_value+= matrix[firstRow+row][firstCol+col]
            if (minSum >sum_value): 
                minSum = sum_value
    return minSum;
n,m=map(int,input().split())
arr=[]
a=[]
sum_arr=[]
for i in range(n):
    a=[int(i) for i in stdin.readline().split()]
    arr.append(a)
print(maxSubSum(arr,3))