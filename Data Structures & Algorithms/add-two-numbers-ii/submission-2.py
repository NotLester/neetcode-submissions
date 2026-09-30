# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = self.get_rev_LL(l1), self.get_rev_LL(l2)
        carry = 0
        dummy_node = ListNode(-1)
        tail = dummy_node

        while l1 or l2 or carry>0:
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
            print(tail.val)
                
        return self.get_rev_LL(dummy_node.next)
    
    def get_rev_LL(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead
        return prev
