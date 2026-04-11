class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left,right]


    def binSearch(self, nums, target, Leftbias):

        L,R = 0, len(nums)-1
        i = -1
        while L<=R:
            
            mid = (L+R)//2

            if nums[mid] > target:
                R = mid-1
            elif nums[mid] < target:
                L = mid+1
            else:
                i = mid
                if Leftbias:
                    R = mid - 1
                else:
                    L = mid + 1 
        return i
        # res = []
        # if len(nums) == 0:
        #     return [-1,-1]
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         res.append(i)
        #     else:
        #         continue
        # if not res:
        #     return [-1,-1]    
        # return [res[0], res[-1]]

        
