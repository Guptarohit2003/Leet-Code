class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        result = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(intervals[i][0], newInterval[0]),
                max(intervals[i][1], newInterval[1]),
            ]
            i += 1
        result.append(newInterval)
        result.extend(intervals[i:])
        return result


print(Solution().insert([[1, 3], [6, 9]], [2, 5]))
