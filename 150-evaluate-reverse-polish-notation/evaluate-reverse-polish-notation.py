class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)  
        }
        for token in tokens:
            if token in ops:
                first = stack.pop()
                second = stack.pop()
                result = ops[token](second, first)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]


        