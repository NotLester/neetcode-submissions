import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        while k and max_heap:
            k -= 1
            largest_gift = - heapq.heappop(max_heap)
            rem_gift = floor(math.sqrt(largest_gift))
            heapq.heappush(max_heap, -rem_gift)

        return sum([-val for val in max_heap])