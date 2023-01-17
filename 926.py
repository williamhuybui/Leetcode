class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
          #solution 2:
        zeros, ones = s.count("0"),0
        res = zeros
        for digit in s:
            if digit == "0":
                zeros -= 1
            else:
                ones += 1
            res = min(res, zeros + ones )
        return res
