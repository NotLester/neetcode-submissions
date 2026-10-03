class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        min_heap = [[x**2 + y**2, [x, y]] for x, y in points]
        heapq.heapify(min_heap)

        for _ in range(k):
            dist, coords = heapq.heappop(min_heap)
            res.append(coords)

        return res