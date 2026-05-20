# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None # none for now
        while head:
            nextNode = head.next
            head.next = previous # point to the previous val
            previous = head # the next prev val for the next node is the current head
            head = nextNode # move onto the next node
        return previous
            