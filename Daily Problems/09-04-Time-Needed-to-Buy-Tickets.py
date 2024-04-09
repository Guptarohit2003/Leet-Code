class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0
        i = 0
        count = 0
        while tickets[k] > 0:
            # print(i)
            if i == k:
                count += 1
                time += count
                tickets[k] -= 1
                # print(count)
                count = 0
            else:
                if tickets[i] > 0:
                    tickets[i] -= 1
                    count += 1
            if i < len(tickets) - 1:
                i += 1
            else:
                i = 0
        return time


print(Solution().timeRequiredToBuy([2, 3, 2], 2))
print(Solution().timeRequiredToBuy([1, 2, 6, 5, 3, 4], 0))
print(Solution().timeRequiredToBuy([5, 1, 1, 1], 0))
