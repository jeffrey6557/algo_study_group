class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        
        if N <= 1 or K <= 1:
            return 0
        
        parent = self.kthGrammar(N-1, K//2+K%2) # return 0 or 1
        if parent:
            # K - 1 because of 0-index
            return [1, 0][(K-1)%2]
        else:
            return [0, 1][(K-1)%2]
            
        