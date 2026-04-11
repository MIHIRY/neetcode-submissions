class Solution:
    def trap(self, height: List[int]) -> int:
        L,R = 0, len(height)-1

        res = 0
        left_max = height[L]
        right_max = height[R]
        if len(height) < 3:
            return 0    
        while L < R:
            if left_max < right_max:
                L = L +1 
                left_max = max(left_max, height[L])
                res = res + left_max - height[L]
            else:
                R = R -1
                right_max = max(right_max, height[R])
                res = res + right_max - height[R]
        return res

            
        
