class Solution:
    def countSubstrings(self, s):
        def helper(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i, j = i - 1, j + 1
            return (j-i)//2
        
        return sum(helper(k,k) + helper(k,k+1) for k in range(len(s)))