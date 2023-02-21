#Method 1
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for e in nums:
            res^=e
        return res
#Method 2
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) // 2
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            idx = mid * 2
            if idx + 1 >= len(nums) or nums[idx] != nums[idx + 1]:
                r = mid - 1
                ans = nums[idx]
            else:
                l = mid + 1
        return ans


# [0,1,2,3,4,5,6,7,8]
# [1,1,2,3,3,4,4,8,8]
# l, r = 0, 4
# 1) 
# m = 2
# idx = 4
# 5 >= 8 or 3 != 4
# r = 1
# ans = 3
# 2)
# m = 0 + 1 //2 = 0
# idx = 0
# l = 1
# 3)
# m = 1
# idx = 2
# 3 >= 8 or 2 != 3
# r = 0
# ans = 2
# 4) 

