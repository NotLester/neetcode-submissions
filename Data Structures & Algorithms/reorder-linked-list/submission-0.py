# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        size = self.get_length(head)
        target_left_size = size - size//2

        left, right = self.split(head, target_left_size)
        right = self.reverse_list(right)
        self.merge(left, right)
    
    def split(self, head: Optional[ListNode], target_left_size: int) -> tuple[ListNode, ListNode]:
        left_i = head
        left_size = 1
        while left_size < target_left_size:
            left_i = left_i.next
            left_size += 1
        
        right = left_i.next
        left_i.next = None
        left = head
        return left, right
    
    def merge(self, left:ListNode, right:ListNode) -> None:
        while left.next and right:
            next_left = left.next
            next_right = right.next
            left.next = right
            right.next = next_left
            left = next_left
            right = next_right
        left.next = right

    def get_length(self, head: Optional[ListNode]) -> int:
        res = 0
        while head:
            res += 1
            head = head.next
        return res
    
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, curr = None, head
        while curr:
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead
        return prev