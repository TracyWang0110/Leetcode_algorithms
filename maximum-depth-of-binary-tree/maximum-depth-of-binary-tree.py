# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #多少层
        #二叉树的高度，所有节点深度的最大值
        #借助递归函数参数
        #遍历时候，求出深度
        
        self.res = 0
        self.helper(root,1) #根结点是1
        
        return self.res
        
    def helper(self,root, height):
        if root is None:
            return 
        self.res = max(self.res, height)
        self.helper(root.left, height+1)
        self.helper(root.right, height+1)
        
    