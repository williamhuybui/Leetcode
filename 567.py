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

#Most efficient one
from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False
            
