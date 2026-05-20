# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.best_path_sum = float("-inf")

        def dfs(node):
            """
            Returns:
                The maximum path sum that starts at this node
                and goes downward in exactly one direction.
                
                In other words, this is the best path this node
                can "contribute" to its parent.
            """
            if node is None:
                return 0

            # Ask left and right children:
            # "What is the best downward path you can give me?"
            left_downward = dfs(node.left)
            right_downward = dfs(node.right)

            # If a child path is negative, it only hurts us, so ignore it.
            usable_left = max(left_downward, 0)
            usable_right = max(right_downward, 0)

            # ----- Paths we can RETURN upward to the parent -----
            # A parent can only continue through ONE side, not both.
            just_node = node.val
            node_plus_left = node.val + usable_left
            node_plus_right = node.val + usable_right

            best_path_to_return = max(just_node, node_plus_left, node_plus_right)

            # ----- Path that is centered at this node -----
            # This is a complete path that may use both sides.
            path_through_node = node.val + usable_left + usable_right

            # Update the global answer if this is the best full path seen so far.
            self.best_path_sum = max(self.best_path_sum, path_through_node)

            return best_path_to_return

        dfs(root)
        return self.best_path_sum



        