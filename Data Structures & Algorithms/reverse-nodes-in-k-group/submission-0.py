# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Orchestrator: Manages the high-level flow of finding, reversing, 
        and reconnecting the k-groups.
        """
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        
        curr = head
        while curr:
            # 1. Check if we have enough nodes for a complete k-group
            kth_node = self.get_kth_node(curr, k)
            if not kth_node:
                break  # Less than k nodes left, leave them as is
            
            # Save the start of the next group before we break the links
            next_group_head = kth_node.next
            
            # 2. Reverse the current k-group
            new_group_head, new_group_tail = self.reverse_k_nodes(curr, k)
            
            # 3. Connect the isolated reversed group back into the main list
            prev_group_tail.next = new_group_head
            new_group_tail.next = next_group_head
            
            # 4. Advance our pointers for the next iteration
            prev_group_tail = new_group_tail
            curr = next_group_head
            
        return dummy.next

    def get_kth_node(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Validator: Moves k-1 steps ahead to verify a group exists and returns its boundary.
        """
        count = 0
        while curr and count < k - 1:
            curr = curr.next
            count += 1
        return curr

    def reverse_k_nodes(self, head: Optional[ListNode], k: int) -> tuple[ListNode, ListNode]:
        """
        Action: Reverses exactly k nodes in isolation. 
        Returns the new head and new tail of this reversed segment.
        """
        prev = None
        curr = head
        
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # After reversing, the original 'head' is now the last node (tail),
        # and 'prev' is the first node (new head).
        return prev, head