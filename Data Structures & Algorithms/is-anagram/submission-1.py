class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            a[s[i]]=1+a.get(s[i],0)
        for i in range(len(s)):
            if t[i] in a:
                a[t[i]]-=1
            else:
                return False
        for c in a.values():
            if c!=0:
                return False
        return True
        
        

        