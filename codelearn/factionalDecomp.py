def check(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a
def factorialDecomp(n):
    item=[]
    for i in range(2,n+1):
        for j in range(2,int(i**(1/2))+1):
            if i%j==0:
                break
        else:
            item.append(i)
    n=check(n)
    value=[]
    for i in item[::-1]:
        d=0
        while (n%i)==0:
            n=int(n//i)
            d+=1
        value.insert(0,d)
    for i in range(len(item)):
        if value[i]>1:
            item[i]='{}^{}'.format(item[i],value[i])
    
    return ' * '.join(map(str,item))
