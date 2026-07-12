class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ss=set()
        for s in nums:
            if s in ss:
                return True
            ss.add(s)
        return False



        