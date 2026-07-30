class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        total=0
        i=0
        ans=[]
        temp=[]
        def dfs(i,total,temp):
            if total==target:
                ans.append(temp.copy())
                return
            if i>=len(nums) or total>target:
                return
            temp.append(nums[i])
            dfs(i,total+nums[i],temp)
            temp.pop()
            dfs(i+1,total,temp)
        dfs(i,total,temp)
        return ans
        


        