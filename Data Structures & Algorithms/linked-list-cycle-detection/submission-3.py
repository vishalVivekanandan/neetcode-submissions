# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # define a fast and slow pointer accordingly
        # while the slow pointer is not null:
            # if pointers are equal, return true
            # iterate each pointer 
        # return false outside while loop

        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


        