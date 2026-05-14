class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [ -cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        # time complexity is O(n * m) where n is the list of tasks and m is the idle time.
        time = 0
        q = deque() #[-cnt, idle time]
        while maxHeap or q:
            time += 1
            if maxHeap:
                # adding one to the count each time we process an element since it will consume 1 cpu time
                cnt = heapq.heappop(maxHeap) + 1 
                if cnt != 0:
                    q.append([cnt, time+n])
            # if the q is not empty and the idle time 
            if q and q[0][1] == time:
                remaining_count = q.popleft()[0]
                # add it back to the heap 
                heapq.heappush(maxHeap,remaining_count)
            elif not maxHeap and q:
                # fast forward idle time, we jump (set the time) to just before the next available time. 
                time = q[0][1] - 1
        return time