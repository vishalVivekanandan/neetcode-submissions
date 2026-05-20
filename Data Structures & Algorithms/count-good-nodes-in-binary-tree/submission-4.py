# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def maxNode(root, maximum):
            if root:
                output = 1 if root.val >= maximum else 0
                maximum = max(maximum, root.val)
                output += maxNode(root.left, maximum)
                output += maxNode(root.right, maximum)
                return output

            return 0

        return maxNode(root, root.val)

            
        