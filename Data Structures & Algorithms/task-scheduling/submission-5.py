class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [] #[-2, -2]
        counter = Counter(tasks)
        for i in counter.values():
            heapq.heappush(maxHeap, -i)

        cooldown = deque()
        t = 0
        while maxHeap or cooldown:
            t += 1
            if maxHeap:
                task = -heapq.heappop(maxHeap)
                if task > 1:
                    cooldown.append([task-1, t+n])
            
            # if the q is not empty and the second element at the head of the queue is equal to the current t
            while cooldown and cooldown[0][1] == t:
                task_count, next_iter = cooldown.popleft()
                heapq.heappush(maxHeap, -task_count)
        return t
                
