# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next # shift slow by one
            fast = fast.next.next #shift fast by two
        
        # why is second, second half of the list?
        second = slow.next
        slow.next = None
        prev = None
        while second:
            # confused... here
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge 
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

