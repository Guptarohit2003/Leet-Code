class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[0])
        arrows = 1
        first_end = points[0][1]

        for x_start, x_end in points:
            if first_end < x_start:
                arrows += 1
                first_end = x_end

        return arrows


print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
