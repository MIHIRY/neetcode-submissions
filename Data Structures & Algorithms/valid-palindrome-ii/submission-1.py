class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(L,R):
            while L < R:
                if s[L] != s[R]:
                    return False
                L = L +1
                R = R-1
            return True
        

        L, R = 0, len(s)-1

        while L < R:
            if s[L] != s[R]:
                return(palindrome(L+1, R) or palindrome(L, R-1))
            L = L + 1
            R = R -1
        return True