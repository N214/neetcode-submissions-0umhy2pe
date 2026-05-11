class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            minHeap.append([distance,point])
        print(f"{minHeap=}")
        heapq.heapify(minHeap)
        while k > 0:
            _, pt = heapq.heappop(minHeap)
            res.append(pt)
            k -= 1
        return res