class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, k = i + 1, len(nums) - 1

            while l < k:
                total = a + nums[l] + nums[k]

                if total == 0:
                    res.append([a, nums[l], nums[k]])
                    l += 1
                    k -= 1

                    # skip duplicates for left pointer
                    while l < k and nums[l] == nums[l - 1]:
                        l += 1

                elif total < 0:
                    l += 1
                else:
                    k -= 1

        return res