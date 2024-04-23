class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves


print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
print(Solution().findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
