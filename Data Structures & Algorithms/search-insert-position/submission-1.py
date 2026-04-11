class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:    
        #         return i
        #     if nums[i]>= target:
        #         return i
            
        # return i+1

        L,R = 0, len(nums)-1

        while L<=R:
            mid = (L+R)//2

            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid -1
            else:
                return mid
        return L