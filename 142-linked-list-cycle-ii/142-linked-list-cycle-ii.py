# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow=fast=head
        start=head
        # pt=ListNode(-1)
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                while slow!=start:
                    slow=slow.next
                    start=start.next
                return start
        return None
               
            
        
        
        