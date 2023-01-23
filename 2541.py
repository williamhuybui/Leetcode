# Slow solution
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        is_add, is_sub = False, False
        
        while True:
            for i in range(len(nums1)):
                if  not is_add and (nums1[i] < nums2[i]):
                    nums1[i] = nums1[i] + k
                    is_add = True
                elif  not is_sub and (nums1[i] > nums2[i]):
                    nums1[i] = nums1[i] - k
                    is_sub = True
            
            if is_add and is_sub:
                res += 1
            if nums1 == nums2:
                return res
            if (not is_add) | (not is_sub):
                return -1
            
            is_add, is_sub = False, False
