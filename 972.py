class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        x1, x2 = 0, 1
        c = 1
        while c < n:
            tmp = x1 + x2
            x1, x2 = x2, tmp
            c += 1
        return tmp
