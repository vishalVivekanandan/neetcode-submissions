"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {} # new graph

        def dfs(node):
            if node in clone: # we've cloned this already so return it
                return clone[node]
            
            # otherwise clone this one
            copy = Node(node.val) 
            clone[node] = copy 
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei)) # clone all of its neighbors
            return copy
            # at this point all nodes of undirected grpahs would be cloned
        
        if node:
            return dfs(node) 
        else:
            return None



        