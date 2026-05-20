"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        copyHash = {}

        i = head
        while i:
            copyHash[i] = Node(i.val)
            i = i.next
        
        i = head
        while i:
            copy = copyHash[i]
            copy.random = copyHash.get(i.random)
            copy.next = copyHash.get(i.next)
            i = i.next

        return copyHash[head]


            

        