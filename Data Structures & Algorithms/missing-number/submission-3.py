class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(0, len(nums)):
        #     if nums[i] != i:
        #         return i
        # return i+1    

        hashset = set(nums)

        for i in range(len(nums)+1):
            if i not in hashset:
                return i