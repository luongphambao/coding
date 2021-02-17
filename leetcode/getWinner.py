class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        curr = arr[0]
        curr_occ = 0
        index = 1
        while curr_occ < k:
            if index == len(arr):
                index = 0
            if curr > arr[index]:
                curr_occ += 1
            else:
                curr = arr[index]
                curr_occ = 1
            index += 1
        return curr