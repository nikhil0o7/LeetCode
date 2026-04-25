class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        # print(ans)
        for index,temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                i, temp = stack.pop()
                ans[i] = index - i
            stack.append([index,temperature])

        return ans
        