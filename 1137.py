class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        
        x1, x2, x3 = 0, 1, 1
        c = 2
        while c < n:
            tmp = x1 + x2 + x3
            x1, x2, x3 = x2, x3, tmp
            c+=1
        return tmp
