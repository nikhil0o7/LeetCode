class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # we need to build a monotonic stack
        # save pair: [temp, index] - we can use index later to update the res

        for i, t in enumerate(temperatures):
        #if we find the current temp is greater than the top element than we pop the top of the stack and set the results variable basically that's what the problem is to find the next top number
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI
            stack.append([t,i])
        return res