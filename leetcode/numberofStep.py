class Solution:
    def numberOfSteps (self, num: int) -> int:
        def solve(num,count):
            if num==0:
                return count
            if num%2==0:
                return solve(num//2,count+1)
            else:
                return solve(num-1,count+1)
        return solve(num,0)
        