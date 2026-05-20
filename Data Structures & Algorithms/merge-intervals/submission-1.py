class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key = lambda i : i[0]) # sort based on keys
        # output = [intervals[0]]
        # for start, end in intervals[1:]:    # skip 1st val because we added it
        #     lastEnd = output[-1][1] # most recently added output's end
        #     if start <= lastEnd:
        #         output[-1][1] = max(lastEnd, end) # it's possible for current output to have a larger end than the last output's end
        #     else:
        #         output.append([start, end]) # otherwise we just add this one without merging
        # return output

        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output