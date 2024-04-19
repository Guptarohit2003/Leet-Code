class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(i: int, j: int) -> None:
            if (
                i < 0
                or j < 0
                or i >= len(grid)
                or j >= len(grid[i])
                or grid[i][j] == "0"
            ):
                return
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands


print(
    Solution().numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)  # 1
