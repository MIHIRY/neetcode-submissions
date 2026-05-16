class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             for k in range(j+1, len(nums2)):
        #                 if nums2[k] > nums2[j]:
        #                     res.append(nums2[k])
        #                     break
                    
        #             else:
        #                 res.append(-1)

        #             break
        # return res

        nums1Idx = {}
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            nums1Idx[nums1[i]] = i
        
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res



                    