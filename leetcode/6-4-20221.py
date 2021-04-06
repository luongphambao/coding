class Solution:
    def isIdealPermutation(self, A):
        level = -float("inf")
        n = len(A)
        for i in range(1, n):
            if A[i] < level: 
                return False
            else:
                level = max(level, A[i-1])
                
        return True