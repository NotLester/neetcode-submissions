# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_A = self.get_length_LL(headA)
        len_B = self.get_length_LL(headB)
        ptr_A, ptr_B = headA, headB

        while len_A > len_B:
            ptr_A = ptr_A.next
            len_A -= 1

        while len_B > len_A:
            ptr_B = ptr_B.next
            len_B -= 1

        while ptr_A != ptr_B:
            ptr_A = ptr_A.next
            ptr_B = ptr_B.next
        
        return ptr_A
    
    def get_length_LL(self, head: ListNode) -> int:
        res = 0
        while head:
            head = head.next
            res += 1
        return res
        