class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, nums: list[int], k: int) -> int:
        res = 0
        freq = {}
        left = 0

        for right, num in enumerate(nums):
            freq[num] = freq.get(num, 0) + 1

            while len(freq) > k:
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            res += right - left + 1

        return res


print(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
print(Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3))
