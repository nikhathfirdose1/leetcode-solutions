# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None
 
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                s = self.succ(root)
                root.val = s.val
                root.right = self.deleteNode(root.right, root.val)
            else:
                p= self.pre(root)
                root.val  = p.val
                root.left = self.deleteNode(root.left, root.val)
        
        return root

    def succ(self,node):
        node = node.right
        while node.left:
            node = node.left

        return node

        
    def pre(self,node):
        node = node.left
        while node.right:
            node = node.right
            
        return node
        