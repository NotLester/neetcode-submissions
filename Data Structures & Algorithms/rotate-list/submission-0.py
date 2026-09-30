# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        
        length = 0
        curr = tail = head
        while curr:
            length += 1
            tail = curr
            curr = curr.next
        
        idx = 0
        k = k % length
        if k == 0:
            return head
        
        dummy = ListNode(0)
        curr = head
        while curr:
            if idx == length - k - 1:
                second_part = curr.next
                curr.next = None
                tail.next = head
                dummy.next = second_part
                return dummy.next
            idx += 1
            curr = curr.next
        
        return None