# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [None]
        count = [0]

        def inorder(root):
            if not root or count == k:
                return
            
            inorder(root.left)

            if count[0] == k:
                return
            
            res[0] = root.val
            count[0] += 1

            inorder(root.right)
        
        inorder(root)
        return res[0]

