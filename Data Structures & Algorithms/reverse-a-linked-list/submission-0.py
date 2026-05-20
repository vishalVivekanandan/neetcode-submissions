# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        x = head
        while x != None:
            nextNode = x.next
            x.next = previous
            previous = x
            x = nextNode
        return previous
            


        