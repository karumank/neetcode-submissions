# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        list_length = 0
        while node:
            list_length += 1
            node = node.next
        
        
        remove_index = abs(list_length - n)
        if remove_index == 0:
            return head.next

        curr = head
        prev = None
        current_index = 0

        while curr:
            if current_index == remove_index:
                prev.next = curr.next
                break

            prev = curr
            curr = curr.next
            current_index += 1

        return head


