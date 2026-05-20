# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
            
        # merge listst in pairs until there's one more left
        while len(lists) > 1:
            output = []
            for i in range(0, len(lists), 2): # we're going through 2 lists per iteration so increment by 2
                l1 = lists[i]
                
                if (i + 1) < len(lists):
                    l2 = lists[i+1]
                else:
                    l2 = None

                output.append(self.mergeSort(l1, l2))
            
            lists = output

        return lists[0]
    
    # took from merge 2 sorted lists
    def mergeSort(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next