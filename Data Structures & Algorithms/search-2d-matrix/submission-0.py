class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [x for row in matrix for x in row]

        L,R = 0, len(nums)-1

        while L<=R:
            mid = (L+R)//2

            if nums[mid] == target:
                return True
            
            
            if nums[mid] < target:
                L = mid + 1
            elif nums[mid] > target:
                R = mid - 1
            else:
                return True
        return False

        