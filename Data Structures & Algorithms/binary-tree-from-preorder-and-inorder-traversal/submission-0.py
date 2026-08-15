# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inOrderMap = {}
        for i in range(len(inorder)):
            inOrderMap[inorder[i]] = i

        preOrderIndex = 0

        def dfs(left, right):
            nonlocal preOrderIndex
            if left > right:
                return None
            
            root_value = preorder[preOrderIndex]
            preOrderIndex += 1

            root = TreeNode(root_value)
            split = inOrderMap[root_value]

            root.left = dfs(left, split - 1)
            root.right = dfs(split + 1, right)

            return root

        
        
        return dfs(0, len(inorder) - 1)

#       In Order   [5, 2, 6, 1, 7, 3, 4]
#       Pre Order  [1, 2, 5, 6, 3, 7, 4]

#           1
#        ↙     ↘
#       2       3
#    ↙   ↘   ↙   ↘
#    5    6 7     4


