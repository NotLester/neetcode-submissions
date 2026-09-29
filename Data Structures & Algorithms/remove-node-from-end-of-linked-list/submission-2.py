# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ll_len = self.get_length(head)

        if n > ll_len:
            return head
        
        if n == ll_len:
            node_to_remove = head
            head = head.next
            node_to_remove.next = None
            return head
        
        curr = head
        for _ in range(ll_len - n - 1):
            curr = curr.next
        
        node_to_delete = curr.next
        curr.next = node_to_delete.next
        node_to_delete.next = None

        return head
    
    def get_length(self, head: Optional[ListNode]):
        count = 0
        while head:
            count += 1
            head = head.next
        return count