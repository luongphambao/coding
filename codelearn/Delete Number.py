def min_number(n,a,b):
    if a<=b:
        return 'empty'
    for i in range(b):
        min1=n
        for j in range(a//2):
            k=n[:j]+n[j+1:]
            if int(k)< int(min1):
                min1=k
        n=min1
    return str(int(min1))