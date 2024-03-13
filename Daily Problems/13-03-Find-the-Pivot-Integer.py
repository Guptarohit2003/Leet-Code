class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 1
        sumleft = left
        right = n
        sumright = right
        if n == 1:
            return 1
        while left < right:
            if sumleft < sumright:
                left += 1
                sumleft += left
            else:
                right -= 1
                sumright += right
            if sumleft == sumright and left + 1 == right - 1:
                return left + 1

        return -1


for i in range(1, 100):
    print(f"{i}:", Solution().pivotInteger(i))
# print(Solution().pivotInteger(1))
# print(Solution().pivotInteger(4))
