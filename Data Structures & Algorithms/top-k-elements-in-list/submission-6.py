class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {}

        for n in nums:
            buckets[n] = buckets.get(n, 0) + 1

        freq = defaultdict(list)

        for num in buckets:
            freq[buckets[num]].append(num)

        result = []

        for frequency in range(len(nums), 0, -1):
            if frequency in freq:
                for num in freq[frequency]:
                    result.append(num)

                    if len(result) == k:
                        return result