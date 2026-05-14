class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        sets = set(nums)

        for n in nums:
            if(n - 1 ) not in sets:
                length = 0
                while(n + length) in sets:
                    length = length + 1
                longest = max(length , longest)

        return longest         