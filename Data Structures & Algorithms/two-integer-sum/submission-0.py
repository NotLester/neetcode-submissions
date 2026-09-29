class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [
                    min(i, hashmap[complement]),
                    max(i, hashmap[complement])
                ]
            hashmap[nums[i]] = i

        return [-1, -1]