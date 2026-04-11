class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(start,dur, idx) for idx,(start,dur) in enumerate(tasks)]
        tasks.sort(reverse = True)
        queued_tasks = []
        next_available_t = 0

        res = []

        while queued_tasks or tasks:

            if not queued_tasks and next_available_t <= tasks[-1][0]:
                next_available_t = tasks[-1][0]


            while tasks and tasks[-1][0] <= next_available_t:
                start,dur,idx = tasks.pop()
                heapq.heappush(queued_tasks, (dur,idx))

            
            dur,idx = heappop(queued_tasks)
            next_available_t += dur
            res.append(idx)
        return res


        