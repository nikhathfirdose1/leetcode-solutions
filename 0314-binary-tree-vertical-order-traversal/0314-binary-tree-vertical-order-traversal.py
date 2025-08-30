# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        column = defaultdict(list)

        queue = deque([(root, 0)])

        ans = []

        while queue:

            node, col = queue.popleft()

            if node is not None:
                column[col].append(node.val)
                queue.append((node.left, col-1))

                queue.append((node.right, col +1))

        
        for col in sorted(column.keys()):
            ans.append(column[col])

        return ans



        