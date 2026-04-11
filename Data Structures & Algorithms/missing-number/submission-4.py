class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Brute Force
        # nums.sort()
        # for i in range(0, len(nums)):
        #     if nums[i] != i:
        #         return i
        # return i+1    

        #HashSET
        # hashset = set(nums)

        # for i in range(len(nums)+1):
        #     if i not in hashset:
        #         return i

        res = len(nums)

        for i in range(len(nums)):
            res = res + i - nums[i]
        return res