# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        tail = dummy_node
        carry = 0

        while l1 or l2 or carry > 0:
            curr_sum = carry

            if l1:
                curr_sum += l1.val
                l1 = l1.next
            if l2:
                curr_sum += l2.val
                l2 = l2.next
            
            carry = curr_sum // 10
            digit = curr_sum % 10

            tail.next = ListNode(digit)
            tail = tail.next
        
        return dummy_node.next

