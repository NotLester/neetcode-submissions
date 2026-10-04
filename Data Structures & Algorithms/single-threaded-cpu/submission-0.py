class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        queue = []
        for idx, task in enumerate(tasks):
            queue.append([task[0], task[1], idx])
        
        queue = deque(sorted(queue))
        minheap = []
        time = 0
        order = []

        while minheap or queue:
            while queue and queue[0][0] <= time:
                enq_time, proc_time, idx = queue.popleft()
                heapq.heappush(minheap, [proc_time, idx])
            
            if minheap:
                proc_time, idx = heapq.heappop(minheap)
                time += proc_time
                order.append(idx)
            else:
                time = queue[0][0]

        return order