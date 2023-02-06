 class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return  [j for i in list(zip(nums[:n],nums[n:])) for j in i]
