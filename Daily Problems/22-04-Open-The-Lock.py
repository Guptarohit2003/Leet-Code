from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
        queue = deque([("0000", 0)])
        while queue:
            current, steps = queue.popleft()
            for i in range(4):
                for j in [-1, 1]:
                    new = (
                        current[:i] + str((int(current[i]) + j) % 10) + current[i + 1 :]
                    )
                    if new == target:
                        return steps + 1
                    if new not in deadends:
                        deadends.add(new)
                        queue.append((new, steps + 1))
        return -1


print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
print(Solution().openLock(["8888"], "0009"))
