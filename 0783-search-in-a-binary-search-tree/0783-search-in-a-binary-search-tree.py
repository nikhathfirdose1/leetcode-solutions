# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                return None

            if node.val == val:
                return node

            elif node.val> val:
                queue.append(node.left)
            else:
                queue.append(node.right)

        return None

        