class Solution:
    def isValid(self, s: str) -> bool:
        h={"{":"}","(":")","[":']'}
        stack=[]
        for c in s:
            if c in h:
                stack.append(c)
            else:
                if stack and h[stack[-1]]==c:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False
        