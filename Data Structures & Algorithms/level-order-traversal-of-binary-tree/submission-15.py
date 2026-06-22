# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            out = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    out.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if out:
                res.append(out)
        return res

                

            


