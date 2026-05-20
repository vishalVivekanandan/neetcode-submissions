# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# You are given the root of a binary tree. 
# Return only the values of the nodes that are visible from the right side of the tree, 
# ordered from top to bottom.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                output.append(rightSide.val)
        return output

            

        
        