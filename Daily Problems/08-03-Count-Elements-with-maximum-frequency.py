class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        max_freq = 0
        max_freq_elements = []
        for num in nums:
            freq = nums.count(num)
            if freq > max_freq:
                max_freq = freq
                max_freq_elements = [num]
            elif freq == max_freq:
                max_freq_elements.append(num)
        return max_freq * len(set(max_freq_elements))


print(Solution().maxFrequencyElements([1, 2, 3, 4, 5]))
