class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        # from 1-n, the count of each
        buckets = defaultdict(list)

        for key in freq:
            buckets[freq[key]].append(key)
        
        # have this run k times
        res = []
        for n in range(len(nums), 0, -1):
            if n in buckets:
                for v in buckets[n]:
                    res.append(v)
                    if len(res) == k:
                        return res
            
            

        


