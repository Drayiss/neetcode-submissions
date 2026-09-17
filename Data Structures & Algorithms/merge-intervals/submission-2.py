class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        merged_intervals = [intervals[0]]

        n = len(intervals)
        for i in range(1, n):
            prev_interval = merged_intervals[-1]
            curr_interval = intervals[i]
            if prev_interval[1] >= curr_interval[0]:
                prev_interval[1] = max(prev_interval[1], curr_interval[1])
            else:
                merged_intervals.append(curr_interval)

        return merged_intervals