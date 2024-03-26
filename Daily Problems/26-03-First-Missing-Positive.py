class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        if not nums:
            return 1

        nums = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i

        return 1
