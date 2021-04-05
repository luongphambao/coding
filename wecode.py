arr = []
while True:
    x = [int(i) for i in input().split()]
    if x == []:
        break
    arr.append(x[0])
def LRN(i):
    if i >= len(arr) // 2:
        print(arr[i])
        return
    LRN(2*i+1)
    LRN(2*i+2)
    print(arr[i])