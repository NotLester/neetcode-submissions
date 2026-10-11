import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, math.ceil(num ** 0.5)

        while left <= right:
            mid = right - (right - left)//2
            mid_sqr = mid * mid

            if mid_sqr == num:
                return True
            
            if mid_sqr > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False