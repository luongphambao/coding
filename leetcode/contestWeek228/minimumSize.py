class Solution(object):
    def minimumSize(self, A, maxOperations):
        def make(bound):
            if bound == 0: return False
            ops = 0
            for x in A:
                q, r = divmod(x, bound)
                if r == 0:
                    ops += q - 1
                else:
                    ops += q
            return ops <= maxOperations
        
        # print([make(b) for b in range(1, 5)])
        lo, hi = 0, max(A)
        while lo < hi:
            mi = lo + hi >> 1
            if not make(mi):
                lo = mi + 1
            else:
                hi = mi 
        return lo