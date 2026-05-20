class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = defaultdict(int)
        res = []
        for n in nums:
            output[n] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, val in output.items():
            (buckets[val].append(key))
        for i in range(len(buckets)-1, 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res
