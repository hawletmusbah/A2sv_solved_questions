class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                topop_t, topop_i = stack.pop()
                result[topop_i] = i - topop_i
            stack.append((t ,i))
        return result