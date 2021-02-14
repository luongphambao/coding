class Solution:
    def minOperations(self, s: str) -> int:
        count1,count2=0,0
        for i in range(len(s)):
            if s[i]=='0':
                if i%2==0:
                    count1+=1
                else:
                    count2+=1
            else:
                if i%2==0:
                    count2+=1
                else:
                    count1+=1
        s1=len(s)-count1
        s2=len(s)-count2
        return min(s1,s2)
                