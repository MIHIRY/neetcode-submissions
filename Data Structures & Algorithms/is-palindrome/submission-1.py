class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []

        for ch in s:
            if ch.isalnum():
                arr.append(ch.lower())
        
        L, R = 0, len(arr) - 1

        while L < R:
            if arr[L] != arr[R]:
                return False
            L +=1
            R -= 1
        return True