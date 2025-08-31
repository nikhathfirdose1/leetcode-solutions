# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        def isLeaf(node):
            return node and not node.left and not node.right
        
        ans = []
        if not isLeaf(root):
            ans.append(root.val)
        
        
        node = root.left
        while node:
            if not isLeaf(node):
                ans.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
        
        
        def addLeaves(node):
            if not node:
                return
            if isLeaf(node):
                ans.append(node.val)
            else:
                addLeaves(node.left)
                addLeaves(node.right)
        
        addLeaves(root)
        
        
        stack = []
        node = root.right
        while node:
            if not isLeaf(node):
                stack.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        ans.extend(reversed(stack))
        
        return ans
