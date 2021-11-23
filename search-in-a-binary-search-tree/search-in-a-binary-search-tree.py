# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #经典遍历题，bsf,dsf 
        #相同点在left还是right
        #迭代
        while root and root.val != val:
            if val<root.val:
                root = root.left
            else:
                root = root.right 
        return root 
        #在root的值等于val，root是个空节点
        #空的树，val不在这个树上的时候，返回none
        #o(h)
        
        #递归的方法：recursion
        #递归三要素
        #递归的定义
        #输入，输出
        #递归的出口
        
        if root is None or root.val==val:
            return root
        #递归的拆解
        if  val < root.val:
            return searchBST(root.left,val)
        else:
            return searchBST(root.right,val)
        
        
    
    
        
    
        