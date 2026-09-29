# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy_node = ListNode(-1)
        dummy_node.next = head
        curr = dummy_node
        while curr.next:
            if curr.next.val == val:
                node_to_delete = curr.next
                curr.next = node_to_delete.next
                node_to_delete.next = None
            else:
                curr = curr.next
        
        return dummy_node.next