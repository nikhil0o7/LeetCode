class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(start,dur,i) for i, (start,dur) in enumerate(tasks)]
        tasks.sort(reverse = True)
        next_available_t = 0
        queued_tasks = []

        ans = []

        while tasks or queued_tasks:

            if not queued_tasks and next_available_t <= tasks[-1][0]:
                next_available_t = tasks[-1][0]


            while tasks and tasks[-1][0] <= next_available_t:
                start,dur,idx = tasks.pop()
                heapq.heappush(queued_tasks, (dur,idx))

            dur,idx = heapq.heappop(queued_tasks)
            next_available_t += dur
            ans.append(idx)

        return ans


        