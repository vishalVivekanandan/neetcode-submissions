class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # each task 1 unit time
        # minimize idle time
        
        # key is Task char, value is count of said char
        count = Counter(tasks)
        print(count)

        maxHeap = [-cnt for cnt in count.values()] # insert each freq # in maxheap
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() # pairs of [-cnt, idleTime until we can process this again]
        
        while maxHeap or q:
            time += 1 
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # decrement the freq of said char
                if cnt:
                    q.append([cnt, time + n]) # we still have more frequencies of it
            if q and q[0][1] == time: # we've reached time to process val in queue
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

