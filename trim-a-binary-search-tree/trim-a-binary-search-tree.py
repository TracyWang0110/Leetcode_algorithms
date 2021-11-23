# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        #依然是个bsf
        #中间节点剪掉，是需要拼接的
        #递归的出口
        if root is None:
            return None
        #判断根节点落在哪里
        root_val = root.val
        #在low和high中间
        if low<=root_val and root_val<=high:
            root.left=self.trimBST(root.left, low, root_val)
            root.right=self.trimBST(root.right,root_val, high)
            return root
        #root < low 
        elif root_val<low:
            return self.trimBST(root.right,low,high)
        #max<root
        else:
            return self.trimBST(root.left,low,high)