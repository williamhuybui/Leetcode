#Method 1
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for e in nums:
            res^=e
        return res
      
