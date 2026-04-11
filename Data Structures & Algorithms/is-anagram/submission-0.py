class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        
        countS, countT = {} , {}

        for c in s:
            countS[c] = countS.get(c, 0) + 1 

        for i in t:
            countT[i] = countT.get(i, 0) + 1

        return countS == countT
            