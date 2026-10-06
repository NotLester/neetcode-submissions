class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_cnt = max_one_cnt = 0
        
        for num in nums:
            one_cnt = (one_cnt + 1 if num == 1 else 0)
            max_one_cnt = max(max_one_cnt, one_cnt)
        
        return max_one_cnt