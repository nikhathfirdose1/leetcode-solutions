# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        res=[]
        left = True

        while queue:
            size = len(queue)
            
            levels = deque()
            for _ in range(size):

                node = queue.popleft()

                if left:
                    levels.append(node.val)
                else:
                    levels.appendleft(node.val)

                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            
            res.append(list(levels))
            left = not left

        return res