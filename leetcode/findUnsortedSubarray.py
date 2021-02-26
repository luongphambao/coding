class Solution:
    def findUnsortedSubarray(self, nums):
        nums = [-float("inf")] + nums + [float("inf")]
        run_max = list(accumulate(nums, max))
        run_min = list(accumulate(nums[::-1], min))[::-1]
        
        end, beg = len(nums) - 1, 0

        while nums[end-1] <= nums[end] and run_max[end-1] <= nums[end - 1]:
            end -= 1
            
        if end == 0: return 0
            
        while nums[beg+1] >= nums[beg] and run_min[beg+1] >= nums[beg + 1]:
            beg += 1
            
        return end - beg - 1