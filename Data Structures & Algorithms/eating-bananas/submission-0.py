class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # given a list of n piles, each with i bananas
        # need to figure out # of banas to eat per hour to eat all bananas in h hours
        # min is 1, max is total amount of bananas

        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l+r)//2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / m)
            if totalTime <= h:
                res = m
                r = m - 1
            else:
                l = m+1
        return res
        