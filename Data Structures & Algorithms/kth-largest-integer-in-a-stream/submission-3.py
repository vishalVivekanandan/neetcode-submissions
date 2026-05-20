class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        # for k largest val, have heap size of k. Always maintain size k by
        # popping min val when size > k
        # this lets us keap k biggest vals
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        
        # # heapify makes the heap valid
        # heapq.heapify(self.minHeap)
        # while len(self.minHeap) > k:
        #     heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        # # add val
        # heapq.heappush(self.minHeap, val)
        
        # # pop if size is too big
        # if len(self.minHeap) > self.k:
        #     heapq.heappop(self.minHeap)
        
        # # return heap
        # return self.minHeap[0]

        # # this muust add el to list
        # # and compare to mac and min val
        
