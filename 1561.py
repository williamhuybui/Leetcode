class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0 
        piles.sort()
        for i in range(len(piles)//3, len(piles), 2):
            res += piles[i]
        return res
