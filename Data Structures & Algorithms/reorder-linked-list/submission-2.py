# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head):
            previous = None
            while head:
                nextNode = head.next
                head.next = previous
                previous = head
                head = nextNode
            return previous

        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half of the list
        second = reverse(slow.next) 
        
        # end slow list, seperating first and 2nd list
        slow.next = None            

        # first half of the list
        first = head

        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2




        
        
        
    
        


