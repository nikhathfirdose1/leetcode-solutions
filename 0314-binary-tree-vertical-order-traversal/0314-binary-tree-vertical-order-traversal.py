# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        queue = deque([(root, 0)])
        columns = defaultdict(list)
        min_c = max_c = 0
        ans = []

        while queue:
            node, col = queue.popleft()

            # print(node, col)

            if node is not None:
                columns[col].append(node.val)
                min_c = min(min_c, col)
                max_c = max(max_c,col)

                queue.append((node.left, col - 1))
                queue.append((node.right, col + 1))


        for col in range(min_c, max_c + 1):
            ans.append(columns[col])

        return ans



        