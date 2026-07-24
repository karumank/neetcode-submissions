# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_set = set()

        node = head

        while node:
            if node in visited_set:
                return True
            visited_set.add(node)
            node = node.next
        
        return False