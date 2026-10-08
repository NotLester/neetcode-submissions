# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode()
        tail = head

        while tail:
            ahead = tail.next

            prev = dummy
            while prev.next and prev.next.val < tail.val:
                prev = prev.next
            
            tail.next = prev.next
            prev.next = tail
            
            tail = ahead
        
        return dummy.next