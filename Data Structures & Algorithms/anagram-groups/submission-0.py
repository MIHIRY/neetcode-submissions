class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for words in strs:
            lst = [0] * 26
            for char in words:
                lst[ord(char) - ord('a')] += 1 
            lst = tuple(lst)
            res[lst].append(words)
        return list(res.values())