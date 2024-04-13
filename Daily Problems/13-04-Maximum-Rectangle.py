class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        heights = [0] * m
        max_area = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []
            for j in range(m + 1):
                while stack and (j == m or heights[j] < heights[stack[-1]]):
                    height = heights[stack.pop()]
                    width = j if not stack else j - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(j)

        return max_area


print(
    Solution().maximalRectangle(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)  # 6
