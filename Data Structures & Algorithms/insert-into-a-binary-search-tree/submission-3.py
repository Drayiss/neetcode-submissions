# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        curr = root

        while curr.left or curr.right:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    break
            elif val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    break

        if val < curr.val:
            curr.left = TreeNode(val)
        else:
            curr.right = TreeNode(val)

        return root