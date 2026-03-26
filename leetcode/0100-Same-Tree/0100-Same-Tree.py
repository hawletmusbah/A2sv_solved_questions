# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # for p
        def preorderTraversal(root):
        
            if not root :
                return [None]
            
            return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)
            

    
        if preorderTraversal(p) == preorderTraversal(q):
            return True
        return False