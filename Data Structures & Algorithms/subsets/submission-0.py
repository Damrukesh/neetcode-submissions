class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=[]
        subset=[]
        i=0
        def dfs(subset,i):
            if i==n:
                ans.append(subset.copy())
                return
            dfs(subset,i+1)
            subset.append(nums[i])
            dfs(subset,i+1)
            subset.pop()
        dfs(subset,i)
        return ans 
            

        