class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers)-1

        while L < R:
            if numbers[L] + numbers[R] != target:
                if numbers[L] + numbers[R] >  target:
                    R = R - 1
                else:
                    L = L + 1
            else:
                res = [L+1,R+1]
                return res