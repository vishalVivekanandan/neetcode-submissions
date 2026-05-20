# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node:
                if node.left or node.right:
                    node.left, node.right = node.right or None, node.left or None
                    dfs(node.left)
                    dfs(node.right)
            else:
                return None
            
            
        
        dfs(root)
        return root
        