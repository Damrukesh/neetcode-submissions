# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s=[]
        def preorder(root):
            if not root:
                s.append("N")
                return
            s.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ",".join(s)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data=data.split(",")
        self.i=0
        def dfs():
            if data[self.i]=="n":
                self.i+=1
                return None
            node=TreeNode(int(data[self.i]))
            i+=1
            root.left=dfs(root.left)
            root.right=dfs(root.right)
            return node
        return root
        
            






