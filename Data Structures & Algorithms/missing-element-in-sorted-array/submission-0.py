class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        value = 0
        
        for i in range(len(nums)):
            if nums[i] == nums[0]:
                continue
                
            if nums[i] - 1 == nums[i - 1]:
                continue
            else:
                value = nums[i - 1] + 1
                
                while value < nums[i]:
                    k -= 1
                    if k == 0:
                        return value
                    value += 1
        
        return nums[-1] + k

        