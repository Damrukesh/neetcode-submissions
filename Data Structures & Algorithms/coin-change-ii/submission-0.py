class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m=len(coins)#rows
        n=amount+1 #cols
        dp=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if j==0:
                    dp[i][j]=1
                    continue
                if j-coins[i]<0:
                    dp[i][j]=dp[i-1][j] if i>0 else 0
                else:
                    if i==0:
                        dp[i][j]=dp[i][j-coins[i]]
                        continue
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
        return dp[m-1][n-1]
