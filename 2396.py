class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def check_palindromic(val : str):
            """Return bool if it is palindromic"""
            return val == val[::-1]

        def base_converter(num, base):
            """Convert input to its corresponding base value"""
            ans = ""
            while num > 0:
                ans = str(num % base) + ans 
                num //= base
            return ans
        
        #Execution
        for base in range(2, n-2+1):
            ans = base_converter(n, base)
            print(ans, base)
            if check_palindromic(ans) == False:
                return False
        return True
