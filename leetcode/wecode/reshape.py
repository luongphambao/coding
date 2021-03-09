def trans(arr, r,c):
    ans = [[0 for i in range(c)] for j in range(r)]
    flat = sum(arr, [])
    if len(flat) != r * c:
        return arr
    for i in range(len(flat)):
        ans[i//c][i%c]=flat[i]
    return ans
m , n = [int(i) for i in input().split()]
r, c = [int(i) for i in input().split()]
arr= []
for i in range(m):
    arr.append([int(j) for j in input().split()])
arr = trans(arr,r,c)
for i in arr:
    print(*i)