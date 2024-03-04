class Solution:
    def bagOfTokensScore(tokens: list[int], power: int) -> int:
        score = 0
        tokens.sort()
        left, right = 0, len(tokens) - 1
        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                left += 1
                score += 1
            elif score > 0 and right - left > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
        return score


print(Solution.bagOfTokensScore(tokens=[100, 200, 300, 400], power=200))
print(Solution.bagOfTokensScore(tokens=[100, 200], power=150))
