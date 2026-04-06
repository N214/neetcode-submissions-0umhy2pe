# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # loop to put the right pointer to the nth position we want
        while n > 0 and right:
            right = right.next
            n-=1
        #keep going until right is a the end of the list
        while right:
            left = left.next
            right = right.next
        
        #delete the node
        left.next = left.next.next

        return dummy.next