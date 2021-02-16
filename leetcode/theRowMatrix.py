class Solution:
        def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
            return nsmallest(k, range(len(mat)), key=lambda i: sum(mat[i]))