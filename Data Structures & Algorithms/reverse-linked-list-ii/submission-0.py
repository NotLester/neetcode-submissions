# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head

        left -= 1
        right -= 1

        dummy_node = ListNode(-1)
        dummy_node.next = head

        if left == 0:
            left_node = head
            before_left_node = dummy_node
        else:
            before_left_node = head
            i = 0
            while before_left_node and i < left-1:
                before_left_node = before_left_node.next
                i += 1
            left_node = before_left_node.next
        
        right_node = head
        i = 0
        while right_node and i < right:
            right_node = right_node.next
            i += 1
        after_right_node = right_node.next

        curr = left_node
        prev = None
        while curr != after_right_node:
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead
        
        before_left_node.next = prev
        left_node.next = after_right_node
        return dummy_node.next