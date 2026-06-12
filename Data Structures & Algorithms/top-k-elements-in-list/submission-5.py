class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a hash to keep track of count of each num
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # get list of nums with specific count
        freq = [[] for i in range(len(nums)+1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res





        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        
        # # all nums that appear 1 time go in freq[1], appear twice go in freq[2], etc...
        # freq = [[] for i in range(len(nums) + 1)]
        # for num, cnt in count.items():
        #     freq[cnt].append(num)

        # res = []
        # for i in range(len(freq) - 1, 0, -1):
        #     # for each num in the highest freq:
        #     for num in freq[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res

        