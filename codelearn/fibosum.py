def fiboSum(n):
    if n==0: return [-1]
    if n==1: return [1]
    total = 0
    fibo = [1]
    f = 1
    while f<=n:
        fibo.append(f)
        f+=fibo[len(fibo)-2]
    fibo.pop(1)
    index = len(fibo)-1
    while sum(fibo)!=n:
        if sum(fibo)-fibo[index] ==n:
            fibo.pop(index)
            return fibo
        elif sum(fibo)-fibo[index] <=n:
            index-=1
        else:
            fibo.pop(index)
            index-=1
    return [-1]