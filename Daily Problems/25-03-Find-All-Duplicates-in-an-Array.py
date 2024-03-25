class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        duplicates = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                duplicates.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return duplicates
