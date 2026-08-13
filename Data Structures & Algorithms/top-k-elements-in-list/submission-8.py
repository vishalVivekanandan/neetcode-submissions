class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        buckets = defaultdict(list)

        for key in freq:
            buckets[freq[key]].append(key)
        
        res = []
        for n in range(len(nums), 0, -1):
            if n in buckets:
                for v in buckets[n]:
                    res.append(v)
                    if len(res) == k:
                        return res
