class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                print(stack, digit)
                stack.pop()
                k -= 1
            stack.append(digit)
        return "".join(stack[: -k or None]).lstrip("0") or "0"


print(Solution().removeKdigits("1432219", 3))
