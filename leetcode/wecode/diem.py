n=int(input())
def countQue(n):
    if n<=4:
        return 4-n
    return n%2
for i in range(n):
    a=int(input())
    print(countQue(a)) 