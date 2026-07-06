# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # the only reason we create a dummy node is if we want to delete the head node!

        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # make r point to nth node
        for _ in range(n):
            right = right.next
        
        # we want nth from end, so move l and r until r reaches end
        while right:
            left = left.next
            right = right.next
        
        # delete left.next
        left.next = left.next.next
        
        return dummy.next
        