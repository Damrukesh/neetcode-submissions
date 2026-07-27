class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)/2
        ss=set()
        ss.add(0)
        for c in nums:
            news=set()
            news.add(0)
            for s in ss:
                news.add(c+s)
                news.add(s)
            ss=news
        if target in ss:
            return True
        return False

        
            


        