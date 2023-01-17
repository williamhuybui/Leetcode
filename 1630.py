class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for x, y in zip(l,r):
            sub = nums[x:y+1]
            sub.sort()
            flag = True
            dist = sub[0] - sub[1]
            for i in range(1,len(sub)-1):
                if sub[i] - sub[i+1] != dist:
                    flag = False
            res.append(flag)
        return res
