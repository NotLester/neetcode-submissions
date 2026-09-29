# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.split_and_merge_LL(
            0, 
            len(lists) - 1, 
            lists
        )
    
    def split_and_merge_LL(self, start:int, end:int, lists:List[Optional[ListNode]]) -> Optional[ListNode]:
        if start > end:
            return None
        if start == end:
            return lists[start]
        
        mid = start + ((end - start) // 2)
        listA = self.split_and_merge_LL(start, mid, lists)
        listB = self.split_and_merge_LL(mid+1, end, lists)
        return self.merge_2_LL(listA, listB)

    def merge_2_LL(self, listA:Optional[ListNode], listB:Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        tail = dummy_node
        ptr_A, ptr_B = listA, listB

        while ptr_A and ptr_B:
            if ptr_A.val <= ptr_B.val:
                tail.next = ptr_A
                ptr_A = ptr_A.next
            else:
                tail.next = ptr_B
                ptr_B = ptr_B.next

            tail = tail.next
        
        if ptr_A:
            tail.next = ptr_A
        elif ptr_B:
            tail.next = ptr_B
        
        return dummy_node.next