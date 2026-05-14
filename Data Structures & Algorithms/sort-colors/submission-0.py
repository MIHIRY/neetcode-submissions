class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        mid = 0
        R = len(nums)-1

        while mid <= R:
            if nums[mid] == 0:
                nums[L], nums[mid] = nums[mid], nums[L]
                L = L + 1
                mid = mid + 1
            elif nums[mid] == 1:
                mid = mid + 1
            else:
                nums[R], nums[mid] = nums[mid], nums[R]
                R = R - 1
                