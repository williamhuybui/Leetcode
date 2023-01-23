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

# Faster solution: 26/49 case
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        c_add, c_sub = 0, 0
        for i in range(len(nums1)):
            if nums1[i] == nums2[i]:
                continue
            elif nums1[i] < nums2[i]:
                while nums1[i] < nums2[i]:
                    nums1[i] += k
                    c_add += 1
                if nums1[i] != nums2[i]:
                    # print('add')
                    return -1
            elif nums1[i] > nums2[i]:
                while nums1[i] > nums2[i]:
                    nums1[i] -= k
                    c_sub += 1
                if nums1[i] != nums2[i]:
                    # print('sub')
                    return -1
        if c_add != c_sub:
            # print('!=', c_add, c_sub)
            return -1
        else:
            return c_add
