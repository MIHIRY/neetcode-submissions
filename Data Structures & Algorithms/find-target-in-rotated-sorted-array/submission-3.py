class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        # L, R = 0, len(nums)-1

        # while L<=R:
        #     mid = (L + R)//2
        #     if target == nums[mid]:
        #         return mid
            
        #     # left portion
        #     if nums[L] <= nums[mid]:
        #         if target > nums[mid] or target < nums[L]:
        #             L = mid +1 
        #         else: 
        #             R = mid - 1
        #     # right portion
        #     else:
        #         if target < nums[mid] or target > nums[R] :
        #             R = mid - 1
        #         else:
        #             L = mid + 1
        # return -1

        L, R = 0, len(nums)-1
        
        while L < R:
            mid = (L+R)//2
            if nums[mid] > nums[R]:
                L = mid + 1
            else: 
                R = mid
        min_i = L

        if min_i == 0:
            L,R = 0, len(nums)-1
        elif target >= nums[0] and target <= nums[min_i - 1]:
            L,R = 0, min_i -1
        else:
            L,R = min_i, len(nums)-1
        
        while L <= R:
            mid = (L+R)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                L = mid + 1
            else:
                R = mid -1 
        return -1