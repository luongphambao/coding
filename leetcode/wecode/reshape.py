m , n = [int(i) for i in input().split()]
r, c = [int(i) for i in input().split()]
if m*n != r*c:
    for i in range(m):
        q = input()
        print(q)
else:
    arr = []
    j =0
    for i in range(m):
        q = input()
        arr += q.split(" ")
        if len(arr) > c:
            print(*arr[:c])
            arr = arr[c:]
            j+=1
    #print(arr)
    #print("j= ",j)
    for x in range(0, r-j):

        print(*arr[x*c:x*c+c])