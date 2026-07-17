class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[n]=True
        while n>=1:
            for word in wordDict:
                if n-1+len(word)<len(s)+1 and s[n-1:n-1+len(word)]==word:
                    dp[n-1]=dp[n-1+len(word)]
                if dp[n-1]:
                    break
            n-=1
        return dp[0]
        
                


    
        