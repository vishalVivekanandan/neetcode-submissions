# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        curr = head

        nexthead, ok = self.findNext(curr, k)
        while ok:
            tail.next = self.reverse(curr, nexthead)
            tail = curr
            curr = nexthead
            nexthead, ok = self.findNext(curr, k) 
        
        tail.next = curr
        return dummy.next


    def reverse(self, head, nexthead):
        prev = nexthead
        curr = head
        while curr != nexthead: 
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
    
    def findNext(self, head, k):
        nextNode = head
        for i in range(k):
            if nextNode is None:
                return None, False
            nextNode = nextNode.next
        return nextNode, True



        