class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def cal_height(node):
            if not node:
                return 0
            
            left_height = cal_height(node.left)
            if left_height == -1:
                return -1
            
            right_height = cal_height(node.right)
            if right_height == -1:
                return -1
                
            if abs(left_height - right_height) > 1:
                return -1  # Use -1 to indicate that the tree is not balanced
            else:
                return max(left_height, right_height) + 1
    

        if not root:
            return True
        left_height = cal_height(root.left)
        right_height = cal_height(root.right)

        if left_height!=-1 and right_height!=-1 and abs(left_height-right_height) <=1:
            return True
        else:
            return False
