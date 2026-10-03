class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(min_heap)

        for i in range(k):
            min_val, i = heapq.heappop(min_heap)
            nums[i] = min_val * multiplier
            heapq.heappush(min_heap, (nums[i], i))

        return nums