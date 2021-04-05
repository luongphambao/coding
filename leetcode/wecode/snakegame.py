
def set_index(i):
    if i%2==1:
        return i-1
    return i+1
def rolate(rol,move):
    if rol =='<':
        if move=='L':
            return "v"
        else:
            return "^"
    if rol =='>':
        if move=='R':
            return "v"
        else:
            return "^"
    if rol=='v':
        if move=='L':
            return ">"
        else:
            return "<"
    if rol=='^':
        if move=='R':
            return ">"
        else:
            return "<"
def moving():
    S
n,m,c=map(int,input().split())
arr=[]
a=['<','>','^','v']
b=[[1,0],[-1,0],[0,1],[0,-1]]
x=-1
y=-1

for i in range(n):
        s=input()
        arr.append(s)
        
        if x==-1:
            for v in a:
                if v in s:

                    x=s.index(v)
                    y=i
                    break
print(len(arr[0]))
c_index=[[x,y]]
x1,y1=x,y
pop_index=-1
index=-1
for i in range(0,c):
    for j in range(0,4) :
        if j!=pop_index:
            new_x,new_y=x1+b[j][0],y1+b[j][1]
            if arr[new_y][new_x]=='*':
                    c_index.append([new_x,new_y])
                    x1,y1=new_x,new_y
                    pop_index=set_index(j)
                    break
print(c_index)