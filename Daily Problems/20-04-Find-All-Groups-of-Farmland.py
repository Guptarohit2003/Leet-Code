class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        def dfs(i: int, j: int, bottom_right: list[int]) -> None:
            if i < 0 or j < 0 or i >= len(land) or j >= len(land[i]) or land[i][j] == 0:
                return
            land[i][j] = 0
            bottom_right[0] = max(bottom_right[0], i)
            bottom_right[1] = max(bottom_right[1], j)
            dfs(i + 1, j, bottom_right)
            dfs(i - 1, j, bottom_right)
            dfs(i, j + 1, bottom_right)
            dfs(i, j - 1, bottom_right)

        farmlands = []
        for i in range(len(land)):
            for j in range(len(land[i])):
                if land[i][j] == 1:
                    top_left = [i, j]
                    bottom_right = [i, j]
                    dfs(i, j, bottom_right)
                    lst = []
                    for a in top_left + bottom_right:
                        lst.append(a)
                    farmlands.append(lst)
        return farmlands


print(Solution().findFarmland([[1, 0, 0], [0, 1, 1], [0, 1, 1]]))
print(Solution().findFarmland([[1, 1], [1, 1]]))
