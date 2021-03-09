n,m=map(int,input().split())
arr=[]
for i in range(n):
    lst1 = [int(item) for item in input().split()] 
    arr.append(lst1)

top,left,bottom,right=map(int,input().split())
roi_arr=[ [0] * m for _ in range(n)]
for i in range(top,bottom+1):
    for j in range(left,right+1):
        roi_arr[i][j]=arr[i][j]
for i in range(n):
    print(*roi_arr[i])