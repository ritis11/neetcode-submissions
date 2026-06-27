# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
                if not p and not q:
                    return True
                elif not p or not q:
                    return False
                elif p.val != q.val:
                    return False
                val = (isSameTree(p.left, q.left)) and (isSameTree(p.right, q.right))
                return val
        if not root:
            return False
        if not subRoot:
            return True
        elif not isSameTree(root, subRoot):
            val = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            return val
        else:
            return True