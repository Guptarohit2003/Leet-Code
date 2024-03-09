class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        common = set(nums1) & set(nums2)
        return min(common) if common else -1


print(
    Solution().getCommon(
        [1, 2, 8, 12, 32, 34, 43, 52, 57, 62, 64, 67, 71, 71, 79, 81, 86, 91, 93, 94],
        [9, 11, 12, 14, 19, 25, 29, 31, 38, 39, 41, 42, 58, 63, 66, 70, 71, 73, 91, 91],
    )
)
