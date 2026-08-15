class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        h={}
        stack=[]
        result=[0]*len(temperatures)
        for i,c in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<c:
                ind=stack.pop()
                result[ind]=i-ind
            stack.append(i)
        return result     

        
        