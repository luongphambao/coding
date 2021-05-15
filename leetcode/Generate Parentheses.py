def generateParenthesis( n):
    ans=list()
    def backtrack(count=0,solution=[]):
        if len(solution)==2*n:
            if count==0:
                ans.append("".join(solution))
            return 
        if count>0:
            solution.append(")")
            backtrack(count-1,solution)
            solution.pop()
        
        solution.append("(")
        backtrack(count +1,solution)
        solution.pop()
    backtrack()
    return ans
n=int(input())
arr=(generateParenthesis(n))
for i in range(len(arr)-1,-1,-1):
    print(arr[i])