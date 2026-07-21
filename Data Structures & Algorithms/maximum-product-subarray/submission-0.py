class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1,m2=1,1
        ans=float("-inf")
        for i in range(len(nums)-1,-1,-1):
            a,b=m1,m2
            m1=max(nums[i],nums[i]*a,nums[i]*b)
            m2=min(nums[i],nums[i]*a,nums[i]*b)
            ans=max(ans,m1)
        return ans
        
        