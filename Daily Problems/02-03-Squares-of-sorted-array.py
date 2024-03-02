def sortedSquares(nums: list[int]) -> list[int]:
    nums2 = [x**2 for x in nums]
    nums2.sort()
    return nums2


print(sortedSquares([-4, -1, 0, 3, 10]))
print(sortedSquares([-7, -3, 2, 3, 11]))
