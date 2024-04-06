class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        for i in stack:
            s[i] = ""
        return "".join(s)


print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
