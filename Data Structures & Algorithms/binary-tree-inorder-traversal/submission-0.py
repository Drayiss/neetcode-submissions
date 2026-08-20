# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorderAppend(root):
            if not root:
                return
            
            inorderAppend(root.left)
            res.append(root.val)
            inorderAppend(root.right)

        inorderAppend(root)

        return res