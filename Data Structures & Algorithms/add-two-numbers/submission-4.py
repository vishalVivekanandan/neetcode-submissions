# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        output2 = ListNode(0)
        ptr = output2
        carry = 0

        while l1 or l2:
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0

            addSum = l1_value + l2_value + carry

            carry = addSum // 10 
            ptr.next = ListNode(addSum % 10)
            ptr = ptr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry != 0:
            ptr.next = ListNode(1)

        return output2.next

        