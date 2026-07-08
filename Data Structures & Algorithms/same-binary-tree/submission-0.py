# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.flag=1
        def doubledfs(p,q):
            if not p and not q:
                return
            if p and q and p.val==q.val: 
                doubledfs(p.left,q.left)
                doubledfs(p.right,q.right)
            else:
                self.flag=0
        doubledfs(p,q)
        if self.flag==0:
            return False
        else:
            return True
            
        