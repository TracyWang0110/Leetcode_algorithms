# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_equal(self,T1,T2):
        if T1 is None and T2 is None:
            return True 
        if T1 is None or T2 is None:
            return False
        
        if T1.val !=T2.val:
            return False
        
        return self.is_equal(T1.left,T2.left) and self.is_equal(T1.right,T2.right)
    #不能直接比较T1T2，比较的是同一个点儿不是具体的值
        
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #所有子树找出来，比一比
        #edge case:空树是非空的子树吗，相等的
        
        if subRoot is None:
            return True
        if root is None:
            return False
        #先做跟，再左，再右，中序，后序都可以
        if self.is_equal(root,subRoot):
            return True 
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
        
        
        
        