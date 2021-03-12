n,m=map(int,input().split())
arr=[]
for i in range(n):
    a1 = list(map(int,input().strip().split()))[:m]
    arr.append(a1)
top,left,bottom,right=map(int,input().split())
#roi_arr=[ [0] * m for _ in range(n)]
x = [0]*m
trai = [0]*left
phai = [0]*(m- right-1)
for i in range(0, top):
    print(*x)
for i in range(top,bottom+1):
    #roi_arr[i][left:right+1] = 
    print(*(trai + arr[i][left:right+1] + phai))
for i in range(bottom+1,n):
    print(*x)