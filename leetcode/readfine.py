f = open('s000.kp','rb')
print(f)
A=1
B=2
C=3
D=4
arr=[B,C,D,A,D,C,A,C,B,C,C,C,B,A,A,C,B,C,A,A,B,B,B,A,C,B,A,C,C,C,B,C,B,D,D,B,A,B,B,C,C,B,A,D,C,B,D,C,A,A,B,C,D,C,A,B,C,D,D,C,A,B,D,D,B,C,A,C,B,B,B,C,B,D,C,A,B,A,C,D,C,A,B,A,A,A,B,D,A,C,B,B,D,A,C,B,D,B,C,D,A,A,D,D,A,A,B,C,D,B,C,B,B,A,D,D,C,D,C,C,A,B,B,C,D,A,A,D,A,B,B,C,A,D,D,C,A,B,A,C,A,B,B,A,D,D,C,A,C,C,B,D,B,B,D,C,B,A,B,B,C,B,D,D,B,C,A,D,C,A,B,D,B,A,D,C,A,D,B,D,A,A,C,C,B,C,C,B,C,A,A,B,D,D,C,B,A,D,C,B]
print(len(arr)) 
b=[B,A,D,A,D,C,A,C,B,C,B,C,B,A,B,C,B,B,C,A,A,A,C,C,C,B,C,C,C,B,A,C,C,D,C,B,A,B,B,C,A,B,A,A,C,D,A,D,A,A,B,C,D,C,C,C,A,C,C,A,A,C,B,C,B,C,A,C,C,C,B,C,A,D,B,C,B,A,C,D,C,A,B,B,A,A,B,A,D,C,B,A,C,A,C,B,D,B,C,D,A,A,A,D,C,A,B,D,C,B,C,B,B,C,D,D,C,D,C,C,C,B,C,D,C,B,A,D,A,D,B,C,A,A,D,D,A,B,D,C,A,B,C,A,B,B,C,A,C,C,B,D,D,B,D,C,B,C,C,D,A,A,C,D,B,C,C,D,C,A,B,D,B,C,D,D,D,D,C,D,A,A,C,D,C,B,B,B,B,B,B,B,B,B,B,A,B,B,B,B]
print(len(b))
c=[B,C,D,A,D,C,C,C,B,C,C,C,B,A,A,C,B,C,A,A,B,B,B,C,C,B,A,C,C,C,B,C,B,D,D,B,A,B,B,C,C,B,A,D,C,B,D,C,D,A,B,D,D,C,A,B,C,D,D,B,A,C,D,D,B,C,D,C,B,B,B,C,B,D,C,A,B,A,C,C,A,A,B,A,A,A,B,C,A,B,B,B,D,A,C,B,D,B,C,D,A,A,C,C,A,A,B,C,D,B,C,B,B,A,D,D,A,D,B,B,A,B,B,C,D,A,A,D,A,B,B,C,D,D,D,C,A,D,A,C,A,B,B,A,D,D,C,A,A,C,B,D,B,B,D,C,B,A,B,B,C,B,D,D,B,C,A,D,C,A,B,D,B,A,B,C,A,D,C,D,A,A,C,D,B,C,C,B,C,A,A,B,D,B,B,B,A,D,B,B]
print(len(c))
def check(arr,c):
    count=0
    for i in range(200):
        if arr[i]!=c[i]:
            count+=1
    return count
print("So cau sai la",check(arr,b))