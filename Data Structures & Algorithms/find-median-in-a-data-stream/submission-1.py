class MedianFinder:

    def __init__(self): # minheap and maxheap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            # python doesnt implement maxheap for small vals by default
            # retrieving the smallest val in a maxheap is possible because the 
            # smallest val becomes the largest val if everything is negated
            heapq.heappush(self.small, -1 * num)
        
        if len(self.small) > len(self.large) + 1:
            # so everytime we pop from this maxheap, we multiply it by -1 to get the og val
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)    
        
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return ((-1 * self.small[0]) + self.large[0]) / 2
        
        