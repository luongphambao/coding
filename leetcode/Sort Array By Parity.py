class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even=[]
        odd=[]
        for i in range(len(A)):
            if A[i]%2==0:
                even.append(A[i])
            else:
                odd.append(A[i])
        return even+odd