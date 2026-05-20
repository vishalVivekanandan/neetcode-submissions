class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclid = []
        for x, y in points:
            dist = math.sqrt((x ** 2) + (y ** 2))
            euclid.append([dist, x, y])
        heapq.heapify(euclid)
        res = []
        
        while k > 0:
            dist, x, y = heapq.heappop(euclid)
            res.append([x, y])
            k -= 1
        return res

        
