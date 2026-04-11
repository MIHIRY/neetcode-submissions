class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
       
        # n = len(nums)

        # temp = [0]* n
        
        # for i in range(len(nums)):
        #     index = 0 
        #     index = (i+k)%n

        #     temp[index] = nums[i]
        # nums[:] = temp

        k = k%len(nums)

        L,R = 0 , len(nums)-1 
        while L < R:
            nums[L] , nums[R] = nums[R] , nums[L] 
            L = L + 1
            R = R-1
        
        
        
        L,R=0, k-1
        while L < R:
            nums[L] , nums[R] = nums[R] , nums[L]
            L = L +1
            R = R -1

        
        L,R = k,len(nums)-1
        while L < R:
            nums[L] , nums[R] = nums[R] , nums[L]
            L = L + 1
            R = R -1
            