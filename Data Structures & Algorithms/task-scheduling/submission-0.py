class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        counter = Counter(tasks)
        min_heap = [(0, freq) for freq in counter.values()]
        heapq.heapify(min_heap)

        while min_heap:
            t = min_heap[0][0]
            if t <= time:
                t, count = heapq.heappop(min_heap)
                count -= 1
                if count > 0:
                    next_time = t + n + 1
                    heapq.heappush(min_heap, (next_time, count))
                time += 1
            else:
                time = t
        
        return time