class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.array, self.k = nums, k
        heapq.heapify(self.array)
        while len(self.array) > k:
            heapq.heappop(self.array)
            

    def add(self, val: int) -> int:
        heapq.heappush(self.array, val)
        while len(self.array) > self.k:
            heapq.heappop(self.array)
        return self.array[0]
            
        
