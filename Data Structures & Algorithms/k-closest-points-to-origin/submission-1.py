class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       # sort the els within points somehow and keep popping it k times in the end
       # how to sort?
       # we could do this computation for every point: sqrt((x1 - x2)^2 + (y1 - y2)^2)).
        # and then sort based on this result

        euclid = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            euclid.append([dist, x, y])
        heapq.heapify(euclid)
        
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(euclid)
            res.append([x, y])
            k -= 1
        return res

