class Solution:
    def letterCasePermutation(self, S):
        def dfs(i, built):
            if i == len(S):
                self.ans.append(built)
                return
            if S[i].isalpha():
                dfs(i+1, built + S[i].lower())
            dfs(i+1, built + S[i].upper())
        
        self.ans = []
        dfs(0, "")
        return self.ans

#solution2
class Solution:
    def letterCasePermutation(self, S):
        return map(''.join, product(*[set([i.lower(), i.upper()]) for i in S]))