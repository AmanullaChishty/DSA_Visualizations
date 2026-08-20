class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []

        for current_index,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                old_index = stack.pop()
                answer[old_index]=current_index-old_index
            stack.append(current_index)
        return answer
