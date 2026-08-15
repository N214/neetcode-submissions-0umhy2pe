import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, time in times:
            graph[u].append((v, time))

        min_time = {}
        min_heap = [(0, k)] #(distance from source to node, node)

        while min_heap:
            time_to_node, node = heapq.heappop(min_heap)
            if node in min_time:
                continue
            min_time[node] = time_to_node
            for nei, nei_time in graph[node]:
                if nei not in min_time:
                    heapq.heappush(min_heap, (time_to_node+ nei_time, nei))
        
        if len(min_time) == n:
            return max(min_time.values())
        return -1