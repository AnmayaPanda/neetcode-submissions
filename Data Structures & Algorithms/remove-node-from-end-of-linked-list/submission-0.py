# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        
        while curr:
            curr = curr.next
            length += 1
        
        count = 1
        start = head
        prev = None
        while start:
            if count == length - n + 1:
                if prev is None:
                    return head.next
                prev.next = start.next
                start.next = None
                return head
            else:
                prev = start
                start = start.next
                count += 1
        return head