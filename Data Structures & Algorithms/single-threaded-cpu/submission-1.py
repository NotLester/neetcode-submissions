class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        result = []

        tasks = [
                (tasks[i][0], tasks[i][1], i) 
                for i in range(len(tasks))
        ]
        tasks.sort()

        pq = []
        i = 0
        time = tasks[i][0]

        while len(result) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(pq, (tasks[i][1], tasks[i][2]))
                i += 1
            if not pq:
                time = tasks[i][0]
                continue
            proc_time, task_id = heapq.heappop(pq)
            result.append(task_id)
            time += proc_time
        
        return result