class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        L = 0
        res = 0
        for R in range(len(s)):
            while s[R] in charset:
                charset.remove(s[L])
                L+=1
            charset.add(s[R])
            res = max(res, R-L+1)
        return res


        