class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = [num for num in nums]
        heapq.heapify(min_heap)

        while len(nums) - k > 0:
            heapq.heappop(min_heap)
            k += 1

        return min_heap[0]        