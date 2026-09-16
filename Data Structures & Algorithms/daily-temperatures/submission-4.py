class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        count=0
        for i,c in enumerate(temperatures):
            while stack and c>stack[-1][0]:
                result[stack[-1][1]]=i-stack[-1][1]
                stack.pop()
            stack.append([c,i])
        return result
        