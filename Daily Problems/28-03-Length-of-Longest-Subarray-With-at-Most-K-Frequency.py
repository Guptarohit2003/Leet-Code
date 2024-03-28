from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        n, left, result = len(nums), 0, 0
        freq = defaultdict(int)

        for right in range(n):
            freq[nums[right]] += 1
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result


print(Solution().maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2))
print(Solution().maxSubarrayLength([1, 4, 4, 3], 1))
