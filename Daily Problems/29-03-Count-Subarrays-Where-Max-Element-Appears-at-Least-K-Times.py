class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        mx, ans, l, r, n = max(nums), 0, 0, 0, len(nums)
        while r < n:
            k -= nums[r] == mx
            r += 1
            while k == 0:
                k += nums[l] == mx
                l += 1
            ans += l
        return ans


print(Solution().countSubarrays([1, 3, 2, 3, 3], 2))
print(
    Solution().countSubarrays(
        [
            28,
            5,
            58,
            91,
            24,
            91,
            53,
            9,
            48,
            85,
            16,
            70,
            91,
            91,
            47,
            91,
            61,
            4,
            54,
            61,
            49,
        ],
        1,
    )
)
