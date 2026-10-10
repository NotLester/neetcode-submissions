class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        
        l, r = 1, n
        while l <= r:
            mid = r - (r-l)//2
            coins = (mid*(mid+1)) // 2

            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(res, mid)

        return res