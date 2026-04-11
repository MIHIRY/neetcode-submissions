class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        if len(nums) == 0:
            return [-1,-1]
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
            else:
                continue
        if not res:
            return [-1,-1]    
        return [res[0], res[-1]]