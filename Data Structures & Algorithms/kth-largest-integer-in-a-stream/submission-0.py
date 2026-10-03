class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self._add_to_heap(num)
    
    def add(self, val: int) -> int:
        self._add_to_heap(val)
        return self.min_heap[0]    

    def _add_to_heap(self, ele: int) -> None:
        heapq.heappush(self.min_heap, ele)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)