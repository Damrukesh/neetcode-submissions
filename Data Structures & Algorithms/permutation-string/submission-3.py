class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needh={}
        for c in s1:
            needh[c]=1+needh.get(c,0)
        need=len(needh)
        have=0
        haveh={}     
        i,j=0,0
        while j<len(s2):
            if j-i==len(s1):
                if s2[i] in needh and haveh[s2[i]]==needh[s2[i]]:
                    have-=1
                haveh[s2[i]]-=1
                i+=1
            haveh[s2[j]]=1+haveh.get(s2[j],0)
            if s2[j] in needh and haveh[s2[j]]==needh[s2[j]]:
                have+=1
                if have==need:
                    return True
            j+=1
        return False

        