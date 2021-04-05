a=[i for i in input().split()]
arr=[i for i in input().split()]
b=input()
index=[]
result=[]
for v in a: 
    result.append([v]*9)
def solve(c,arr):
    up,bottom,left,right=list(arr[0]),list(arr[1]),list(arr[2]),list(arr[3])
    if c=="U":
        arr[0][0]=right[8]
        arr[2][4]=up[0]
        arr[3][8]=left[4]
    elif c=="U'":
        arr[0][0]=left[4]
        arr[2][4]=right[8]
        arr[3][8]=up[0]
    elif c=="u":
        arr[0][0]=right[8]
        arr[2][4]=up[0]
        arr[3][8]=left[4]
        # 3dinh duoi
        arr[0][1]=right[3]
        arr[0][2]=right[7]
        arr[0][3]=right[6]
        arr[2][6]=up[1]
        arr[2][5]=up[2] 
        arr[2][1]=up[3]
        
        arr[3][3]=left[6]
        arr[3][7]=left[5]
        arr[3][6]=left[1]

    elif c=="u'":
        arr[0][0]=left[4]
        arr[2][4]=right[8]
        arr[3][8]=up[0]
        # 3dinh duoi
        arr[0][1]=left[6]
        arr[0][2]=left[5] 
        arr[0][3]=left[1]
        arr[2][6]=right[3]
        arr[2][5]=right[7]
        arr[2][1]=right[6]
        arr[3][3]=up[1]
        arr[3][7]=up[2]
        
        arr[3][6]=up[3]
        
    elif c=="R":
        arr[0][8]=bottom[4]
        arr[1][4]=right[0]
        arr[3][0]=up[8]
    elif c=="r":
        arr[0][8]=bottom[4]
        arr[1][4]=right[0]
        arr[3][0]=up[8]
        #3dinh duoi
        arr[0][3]=bottom[6]
        arr[0][7]=bottom[5]
        arr[0][6]=bottom[1]
        arr[1][6]=right[1]
        arr[1][5]=right[2] 
        arr[1][1]=right[3]
        arr[3][1]=up[3]
        arr[3][2]=up[7]
        arr[3][3]=up[6]
    elif c=="R'":
        arr[0][8]=right[0]
        arr[1][4]=up[8]
        arr[3][0]=bottom[4]
    elif c=="r'":
        arr[0][8]=right[0]
        arr[1][4]=up[8]
        arr[3][0]=bottom[4]
        #3 DINH CON LAI 
        arr[0][3]=right[1]
        arr[0][7]=right[2]
        arr[0][6]=right[3]
        arr[1][6]=up[3]
        arr[1][5]=up[7]
        arr[1][1]=up[6]
        arr[3][1]=bottom[6]
        arr[3][2]=bottom[5]
        arr[3][3]=bottom[1]
    
    elif c=="B":
        arr[1][0]=left[8]
        arr[2][8]=right[4]
        arr[3][4]=bottom[0]
    elif c=="B'":
        arr[1][0]=right[4]
        arr[2][8]=bottom[0]
        arr[3][4]=left[8]
    elif c=="b":
        arr[1][0]=left[8]
        arr[2][8]=right[4]
        arr[3][4]=bottom[0]
        #
        arr[1][1]=left[3]
        arr[1][2]=left[7]
        arr[1][3]=left[6]
        arr[2][3]=right[6]
        arr[2][7]=right[5]
        arr[2][6]=right[1]
        arr[3][6]=bottom[1]
        arr[3][5]=bottom[2]
        arr[3][1]=bottom[3]
    elif c=="b'":
        arr[1][0]=right[4]
        arr[2][8]=bottom[0]
        arr[3][4]=left[8]
        #aaa =
        arr[1][1]=right[6]
        arr[1][2]=right[5]
        arr[1][3] =right[1]
        arr[2][3]=bottom[1]
        arr[2][7]=bottom[2]
        arr[2][6]=bottom[3]
        arr[3][6]=left[3]
        arr[3][5]=left[7]
        arr[3][1]=left[6]
    elif c=="L":
        arr[2][0]=bottom[8]
        arr[0][4]=left[0]
        arr[1][8]=up[4]
    elif c=="L'":
        arr[2][0]=up[4]
        arr[0][4]=bottom[8]
        arr[1][8]=left[0]
    elif c=="l":
        arr[2][0]=bottom[8]
        arr[0][4]=left[0]
        arr[1][8]=up[4]
        #kjaafsksad
        arr[2][1]=bottom[3]
        arr[2][2]=bottom[7]
        arr[2][3]=bottom[6]
        arr[0][6]=left[1]
        arr[0][5]=left[2]
        arr[0][1]=left[3]
        arr[1][3]=up[6]
        arr[1][7]=up[5]
        arr[1][6]=up[1]
    elif c=="l'":
        arr[2][0]=up[4]
        arr[0][4]=bottom[8]
        arr[1][8]=left[0]
        #aaa
        arr[0][6]=bottom[3]
        arr[0][5]=bottom[7]
        arr[0][1]=bottom[6]
        arr[1][3]=left[1] 
        arr[1][7]=left[2]
        arr[1][6]=left[3]
        arr[2][1]=up[6]
        arr[2][2]=up[5]
        arr[2][3]=up[1]
    return arr 

for c in range(len(arr)-1,-1,-1):
    result=solve(arr[c],result)
for v in result:
    print(*v)