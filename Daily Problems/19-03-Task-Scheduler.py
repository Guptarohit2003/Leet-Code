class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        task_dict = {}
        for task in tasks:
            if task in task_dict:
                task_dict[task] += 1
            else:
                task_dict[task] = 1
        task_list = list(task_dict.values())
        task_list.sort(reverse=True)
        max_task = task_list[0]
        max_count = task_list.count(max_task)
        return max(len(tasks), (max_task - 1) * (n + 1) + max_count)


print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(Solution().leastInterval(["A", "C", "A", "B", "D", "B"], 0))
