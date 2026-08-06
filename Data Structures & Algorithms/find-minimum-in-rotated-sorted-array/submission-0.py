class Solution:
    def findMin(self, nums: List[int]) -> int:
        i,j=0,len(nums)-1
        while i<=j:
            m=(i+j)//2
            if i==m:
                return min(nums[i],nums[j])
            if nums[i]<=nums[m] and nums[m]<nums[j]:
                return nums[i]
            if nums[i]<=nums[m]:
                i=m+1
            else: 
                j=m
        return nums[i]