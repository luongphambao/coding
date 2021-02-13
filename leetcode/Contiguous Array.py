'''
w: Counter, introduce a variable to record the number of 1 and 0
    we met so far
h: 1) if we meet 1, we increase the preSum by 1
   2) otherwise, decrease it by 1
       1) when we met the same preSum later, we know
            the number of 1 and 0 is the same in
            this range
   3) if we meet preSum = 0 later, we know that the number of
        1 and 0 is equal from current index to the begining.
'''

def findMaxLength( nums):
    preSum=0
    count={}
    res=0
    for idx,num in enumerate(nums):#idx la vi tri
        if num==0: 
            preSum+=1
        else: 
            preSum-=1
        if preSum==0: #so luong 0 va 1 bang nhau 
            res=max(res,idx+1)
         # we only store the idx we first met
            # since this would give us the longest 
            # range if we met the same preSum
            # again for second, third... time
        if preSum not in count:
            count[preSum]=idx
        else: 
            res=max(res,idx-count[preSum])
    return res         