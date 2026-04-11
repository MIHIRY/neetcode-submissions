class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in nums:
        #     square = i*i
        #     res.append(square)
        # return sorted(res)

        L,R = 0, len(nums)-1
        res = []
        while L <=R:
            if nums[L]*nums[L] < nums[R]*nums[R]:
                res.append(nums[R]*nums[R])
                R = R-1
            else:
                res.append(nums[L]*nums[L])
                L = L + 1
        return res[::-1]       