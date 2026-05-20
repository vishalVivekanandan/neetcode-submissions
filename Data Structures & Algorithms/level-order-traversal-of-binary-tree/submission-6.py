# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(node):
            queue = collections.deque()
            queue.append(root)

            while queue:
                iter = len(queue)
                level = []
                for i in range(iter):
                    node = queue.popleft()
                    if node:
                        level.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                if level:
                    res.append(level)
                
        bfs(root)
        return res



