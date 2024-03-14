class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = 0
        sum = 0
        sum_dict = {0: 1}
        for num in nums:
            sum += num
            if sum - goal in sum_dict:
                count += sum_dict[sum - goal]
            if sum in sum_dict:
                sum_dict[sum] += 1
            else:
                sum_dict[sum] = 1
        return count


print(Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2))
