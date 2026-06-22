# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # To avoid losing track of the rest of the list, we keep three pointers:

    # curr → the current node we are processing
    # prev → the node that should come after curr once reversed
    # temp → the original next node (so we don't break the chain)
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
