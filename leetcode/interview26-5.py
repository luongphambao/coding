def isMonotonic(nums):
        new_arr=[]
        for  i in range(1,len(nums)):
            new_arr.append(nums[i]-nums[i-1])
        count1=0
        count2=0
        for i in new_arr:
            if i>0:
                count1+=1
            if i==0:
                count1+=1
                count2+=1
            if i<0:
                count2+=1
        if count1==len(new_arr) or count2==len(new_arr):
            return True
        return False
nums=[6,5,4,4]
print(isMonotonic(nums))