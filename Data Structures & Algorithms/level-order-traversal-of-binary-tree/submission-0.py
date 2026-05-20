# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # we need a queue for bfs (insert elements in fifo order)
            # add first element (root) to the queue *initialization
            output = []
            queue = collections.deque()
            queue.append(root)

            # we will pop the queue, but when we add all of its children
            while queue:
                qLen = len(queue)
                level = []
                for i in range(qLen):
                    node = queue.popleft()
                    if node:
                        level.append(node.val)
                        queue.append(node.left)
                        queue.append(node.right)
                if level:
                    output.append(level)
            return output

