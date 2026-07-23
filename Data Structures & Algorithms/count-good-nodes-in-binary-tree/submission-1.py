# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        result_count = 0
        def dfs(node, max_value):
            nonlocal result_count

            if node is None:
                return None
            
            max_value = max(node.val, max_value)

            if node.val >= max_value:
                result_count += 1
            
            dfs(node.left, max_value)
            dfs(node.right, max_value)

        dfs(root, float("-inf"))
        return result_count