class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        difference = (arr[-1] - arr[0]) // len(arr)
        
        for i in range(1, len(arr)):
            if difference == 0:
                return arr[0]

            if arr[i] - arr[i-1] != difference:
                return arr[i-1] + difference