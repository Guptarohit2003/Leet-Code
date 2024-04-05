class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


print(Solution().makeGood("leEeetcode"))
print(Solution().makeGood("abBAcC"))
print(Solution().makeGood("s"))
