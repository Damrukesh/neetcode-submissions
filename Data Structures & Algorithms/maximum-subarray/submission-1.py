class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        j=1
        ans=nums[0]
        temp=nums[0]
        while j<len(nums):
            if temp+nums[j]<0:
                temp=max(nums[j],nums[j]+temp)
                ans=max(ans,temp)
                temp=0

            else:
                temp+=nums[j]
                ans=max(ans,temp)
            j+=1
        return ans
        