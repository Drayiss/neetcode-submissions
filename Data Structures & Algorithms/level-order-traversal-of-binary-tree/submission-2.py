# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def inorderDfs(root, depth):
            if not root:
                return

            if len(res) == depth:
                res.append([])
            
            res[depth].append(root.val)
            
            inorderDfs(root.left, depth + 1)
            inorderDfs(root.right, depth + 1)

        inorderDfs(root, 0)

        return res