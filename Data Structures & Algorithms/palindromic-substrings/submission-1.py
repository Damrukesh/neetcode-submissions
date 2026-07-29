class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            a,b=i,i
            while a>=0 and b<len(s):
                if s[a]==s[b]:
                    ans+=1
                    a-=1
                    b+=1
                else:
                    break
            a,b=i,i+1
            while a>=0 and b<len(s):
                if s[a]==s[b]:
                    ans+=1
                    a-=1
                    b+=1
                else:
                    break
        return ans