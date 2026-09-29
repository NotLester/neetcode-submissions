# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        mid_node = self.get_middle_node_LL(head)
        rev_head = self.get_reversed_LL(mid_node)

        while head and rev_head:
            if head.val != rev_head.val:
                return False
            
            head = head.next
            rev_head = rev_head.next
        
        return True
    
    def get_middle_node_LL(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def get_reversed_LL(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead
        return prev