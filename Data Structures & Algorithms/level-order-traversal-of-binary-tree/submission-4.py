# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, depth):
            if not node:
                return None

            if len(res) == depth:
                res.append([])

            res[depth].append(node.val) # [[1]]

            dfs(node.left, depth+1) # [[1], [2]] -> [[1], [2], [4]] -> ...
            dfs(node.right, depth+1) # [[1], [2, 3]] -> [[1], [2,3], [4,5]] -> ...

        dfs(root, 0)
        return res

