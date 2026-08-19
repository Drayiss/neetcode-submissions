# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 3 cases: no node, node with 0 or 1 children, node with 2 children
        def findMinNode(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        if not root:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            nodeToDelete = root
            if not nodeToDelete.left:
                return nodeToDelete.right
            elif not nodeToDelete.right:
                return nodeToDelete.left
            else:
                # move left subtree to inorder successor's left, then return root.right
                right_min = findMinNode(nodeToDelete.right)
                right_min.left = nodeToDelete.left
                return nodeToDelete.right
            
        return root