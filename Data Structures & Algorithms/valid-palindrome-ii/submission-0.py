class Solution:
    def validPalindrome(self, s: str) -> bool:
        arr = []

        for ch in s:
            if ch.isalnum():
                arr.append(ch)
        
        L,R = 0, len(arr)-1

        while L < R:
            if arr[L] != arr[R]:
                skipL, skipR = arr[L + 1 : R + 1], arr[L: R]
                return(skipL == skipL[::-1] or skipR == skipR[::-1])
            L = L + 1
            R = R -1 
        return True