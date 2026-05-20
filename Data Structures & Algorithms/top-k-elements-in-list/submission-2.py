class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        output = defaultdict(int)
        for i in nums:
            output[i] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for n, f in output.items():
            buckets[f].append(n)

        for f in range(len(buckets) - 1, 0, -1):
            for i in buckets[f]:
                res.append(i)
                if len(res) == k:
                    return res

        
        