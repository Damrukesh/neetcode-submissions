class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations=["+","-","*","/"]
        for c in tokens:
            if c in operations:
                n2=stack.pop()
                n1=stack.pop()
                if c=="+":
                    res=n1+n2
                if c=="-":
                    res=n1-n2
                if c=="*":
                    res=n1*n2
                if c=="/":
                    res=int(n1/n2)
                stack.append(res)
            else:
                stack.append(int(c))
        return stack[0]
            