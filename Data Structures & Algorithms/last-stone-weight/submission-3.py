class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a heap, put the stones
        # inverse the minheap to maxheap to get the two heaviest stone
        # add it back to the heap
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        while len(maxHeap) > 1:
            x, y = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            newStone = -x + y 
            if newStone != 0:
                heapq.heappush(maxHeap, -newStone)
        #print(f"{maxHeap=}")
        return -maxHeap[0] if maxHeap else 0