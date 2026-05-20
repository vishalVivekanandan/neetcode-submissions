class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0   # (height, diameter)

            left_height, left_diameter = dfs(node.left)
            right_height, right_diameter = dfs(node.right)

            height = 1 + max(left_height, right_height)
            through_node = left_height + right_height
            diameter = max(through_node, left_diameter, right_diameter)

            return height, diameter

        return dfs(root)[1]