class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_ele = -1
        freq = 0

        for num in nums:
            if freq == 0:
                maj_ele = num
            freq += (+1 if num == maj_ele else -1)
        
        return maj_ele