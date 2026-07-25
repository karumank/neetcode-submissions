# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [(p, q)]

        while queue:
            node1, node2 = queue.pop(0)
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            if node1.left or node2.left:
                queue.append((node1.left, node2.left))
            if node1.right or node2.right:
                queue.append((node1.right, node2.right))
        return True