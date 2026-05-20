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
            if node is None:
                return 0

            left_downward = dfs(node.left)
            right_downward = dfs(node.right)
            
            # dont take negative paths
            usable_left = max(left_downward, 0)
            usable_right = max(right_downward, 0)

            just_node = node.val
            node_plus_left = node.val + usable_left
            node_plus_right = node.val + usable_right

            # node can only continue through one side
            best_path_to_return = max(just_node, node_plus_left, node_plus_right)

            # Path if we take both sides with this node
            path_through_node = just_node + usable_left + usable_right
            
            # update global max is this surpasses current max
            self.best_path_sum = max(self.best_path_sum, path_through_node)

            # the value we care about for this node
            return best_path_to_return

        dfs(root)
        return self.best_path_sum



        