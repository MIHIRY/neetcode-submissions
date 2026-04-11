class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        pre = [0] * leng
        suf = [0] * leng
        res = [0] * leng

        pre[0] = 1
        suf[leng-1] = 1

        for i in range(1, leng):
            pre[i] = nums[i-1] * pre[i-1]

        for j in range(leng -2 , -1 ,-1):
            suf[j] = nums[j + 1] * suf[j+1]

        for i in range(leng):
            res[i] = pre[i] * suf[i]
        
        return res

        