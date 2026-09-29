# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # get middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the LL starting from mid node
        prev, curr = None, slow
        while curr:
            ahead = curr.next
            curr.next = prev
            prev = curr
            curr = ahead

        # get max sum using 2-pointers from head and mid
        max_sum = -math.inf
        while prev:
            max_sum = max(max_sum, head.val + prev.val)
            head = head.next
            prev = prev.next

        return max_sum
