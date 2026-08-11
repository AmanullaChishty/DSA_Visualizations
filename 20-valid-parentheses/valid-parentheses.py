class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for val in s:
            if val in ['(', '[', '{']:
                stack.append(val)
            else:
                if not stack:
                    return False
                else:
                    if matching[val]==stack[-1]:
                        stack.pop()
                    else:
                        return False
        return not stack
        
        