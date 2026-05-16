class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = {}
        magazine_map = {}

        for ch in ransomNote:
            ransom_map[ch] = ransom_map.get(ch,0) + 1
        
        for ch in magazine:
            magazine_map[ch] = magazine_map.get(ch,0) + 1
        

        for ch in ransom_map:
            if magazine_map.get(ch,0) < ransom_map[ch]:
                return False
        return True