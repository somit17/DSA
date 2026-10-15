class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        ans = [0] * len(temperatures)
        stack = []

        for r in range(len(temperatures)-1,-1,-1):
            current_temp = temperatures[r]

            while stack and current_temp >= temperatures[stack[-1]]:
                stack.pop()
            
            if stack:
                ans[r] = stack[-1] - r
            
            stack.append(r)
        
        return ans