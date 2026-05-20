class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            # output[i] = output[i] + 1 if i in output else 1 
            output[i] = output.get(i, 0) + 1
        
        for key, value in output.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
        