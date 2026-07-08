class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 0
        ans=[0,0]
        for a in range(len(s)):
            i,j=a,a
            while i>=0 and j<len(s) and s[i]==s[j]:
                if j-i>=ans[1]-ans[0]:
                    ans=[i,j]
                i-=1
                j+=1
            i,j=a,a+1
            while i>=0 and j<len(s) and s[i]==s[j]:
                if j-i>=ans[1]-ans[0]:
                    ans=[i,j]
                i-=1
                j+=1
        return s[ans[0]:ans[1]+1]

        