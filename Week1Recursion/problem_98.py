# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, left_bound=None, right_bound=None):
            if not node:
                return True
            # because the left-right grandchild or right-left grandchild is
            # constrained by the grand parent, we need to consider the bounds separately
            left_child = node.left 
            right_child = node.right
            left = True
            if left_child: 
                left = node.left.val < node.val
                if left_bound is not None:
                    left &= left_bound < node.left.val
                if right_bound is not None:
                    left &= right_bound > node.left.val
                left &= helper(node.left, left_bound, node.val) 
            
            right = not node.right 
            if not right: 
                right = node.right.val > node.val
                if left_bound is not None:
                    right &= left_bound < node.right.val
                if right_bound is not None:
                    right &= right_bound > node.right.val
                right &= helper(node.right, node.val, right_bound)  
            return left and right
        
        return helper(root)