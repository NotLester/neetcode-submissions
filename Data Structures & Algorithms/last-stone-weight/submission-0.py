class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            largest = - heapq.heappop(max_heap)
            s_largest = - heapq.heappop(max_heap)
            rem = largest - s_largest
            if rem > 0:
                heapq.heappush(max_heap, -rem)
        
        return -max_heap[0] if max_heap else 0