# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_map = set()

        curr = headA
        while curr:
            node_map.add(curr)
            curr = curr.next
        
        curr = headB
        while curr:
            if curr in node_map:
                return curr
            curr = curr.next
        
        return None
