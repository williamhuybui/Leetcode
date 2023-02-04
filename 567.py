#Exceeding time solution

from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_list = ["".join(List) for List in permutations(s1)]
        l1, l2 = len(s1), len(s2)
        for i in range(l2-l1+1):
            if s2[i:i+l1] in s1_list:
                return True
        return False

#Better one using sorted O(nlog(n))
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        l1, l2 = len(s1), len(s2)
        for i in range(l2-l1+1):
            if s1 == sorted(s2[i:i+l1]):
                return True
        return False
