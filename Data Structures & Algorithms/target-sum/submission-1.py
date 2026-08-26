class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        i=0
        n=len(nums)
        s=0
        self.count=0
        dp={}
        def dfs(i,s):
            if i==n:
                if s==target:
                    return 1
                return 0
            if (i,s) in dp:
                return dp[(i,s)]
            dp[(i,s)]=dfs(i+1,s+nums[i])+dfs(i+1,s-nums[i])
            return dp[(i,s)]
        return dfs(0,0)
        


        