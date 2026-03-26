# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(s,t):
            def preorderTraversal(root):
                if not root :
                        return [None]
                    
                return [root.val] + preorderTraversal(root.left) + preorderTraversal(root.right)
                    

        
            if preorderTraversal(s) == preorderTraversal(t):
                return True
            return False
                    
        
        if not root:
            return False
        
    
        if isIdentical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)