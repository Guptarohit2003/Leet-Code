class Solution:
    def minimumLength(s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            char = s[left]
            while left <= right and s[left] == char:
                left += 1
            while left <= right and s[right] == char:
                right -= 1
        return right - left + 1 if right >= left else 0


print(Solution.minimumLength(s="ca"))
print(Solution.minimumLength(s="cabaabac"))
print(Solution.minimumLength(s="aabccabba"))
