class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q=deque()
        ans=[]
        i=j=0
        while j<len(nums):
            while q and q[-1]<nums[j]:
                q.pop()
            q.append(nums[j])
            if j-i+1==k:
                ans.append(q[0])
                if nums[i]==q[0]:
                    q.popleft()
                i+=1
            j+=1
        return ans
            
