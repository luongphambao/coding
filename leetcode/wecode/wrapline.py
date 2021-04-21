from sys import stdin
s=stdin.readline()
arr=[]
index=0
n1=len(s)
while(index<n1):
    if s[index]!=" ":
        a=s.index(" ",index+1)
        arr.append(s[index:a+1])
        break
m=int(input())
n=len(arr)
if len(s)<=m:
    print(s)
for i in range(n-1): 
    arr[i]+=" "
i=0
while(i<n):
    len_hang=arr[i]
    if i==n-1:
        print(arr[i])
        i+=1
        break
    s=len(len_hang)
    if s<m:
        if s==m-1:
            print(arr[i])
            i+=1
        else:
            for j in range(i+1,n):
                new_len=len_hang+arr[j]
                s1=len(new_len)
                if s1>m:
                    print(len_hang)
                    i=j
                    break
                else:
                    len_hang=new_len
                    if j==n-1:
                        print(new_len)
                        i=n
                        break
        
    else:
        print(arr[i])
        i+=1