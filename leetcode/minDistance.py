def minDistance(self, word1: str, word2: str) -> int:
    	def solve(w1, w2, i, j):
            if i == L1 and j == L2 : return 0
            if i == L1 or j == L2 : 
                return max(L1 - i, L2 - j)
            if w1[i] == w2[j] : 
                return solve(w1, w2, i + 1, j + 1)                
            return 1 + min(solve(w1, w2, i + 1, j), solve(w1, w2, i, j + 1))
	L1, L2 = len(word1), len(word2)
	return solve(word1, word2, 0, 0)   