class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for val in s:
            if not stack:
                stack.append(val)
            elif stack[-1]==val:
                stack.pop()
            else:
                stack.append(val)
        return "".join(stack)