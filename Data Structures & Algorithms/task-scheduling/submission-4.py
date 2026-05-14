class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        heap = []
        # Cooldown queue: each element is a tuple (remaining_count_after_this_run, ready_time)
        cooldown = deque()

        timer = 0 

        for key, value in freq.items():
            heapq.heappush(heap, -value)

        # Main loop: continue while there are tasks to run or tasks cooling down
        while heap or cooldown:
            if heap:
                # Take the most frequent available task
                task = -heapq.heappop(heap)

                # If more instances of this task remain, put it into cooldown
                # ready_time = timer + n + 1
                # Interpretation: after this cycle (at timer), the task will need n idle/cycles
                # and will be ready again after n+1 cycles from the current time.
                if task > 1:
                    cooldown.append((task - 1, timer + n + 1))

            # Advance time by one cycle
            timer += 1

            # Check if any task finishes cooldown at this exact time
            while cooldown and cooldown[0][1] == timer:
                task_count, next_iteration = cooldown[0]
                cooldown.popleft()
                # Push the task back to the heap with its remaining count
                heapq.heappush(heap, -task_count)

        return timer