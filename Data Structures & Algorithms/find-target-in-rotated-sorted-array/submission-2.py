class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        L, R = 0, len(nums)-1

        while L<=R:
            mid = (L + R)//2
            if target == nums[mid]:
                return mid
            
            # left portion
            if nums[L] <= nums[mid]:
                if target > nums[mid] or target < nums[L]:
                    L = mid +1 
                else: 
                    R = mid - 1
            # right portion
            else:
                if target < nums[mid] or target > nums[R] :
                    R = mid - 1
                else:
                    L = mid + 1
        return -1
