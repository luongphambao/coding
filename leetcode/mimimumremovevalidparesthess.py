class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        A,S=list(s),[]
        for i,c in enumerate(A):
            if c not in ['(',')']: pass
            elif c=='(': S.append(i)
            elif S: S.pop()
            else: A[i]=''
        for i in S:
            A[i]=''
        return ''.join(A)