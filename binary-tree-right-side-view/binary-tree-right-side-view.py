# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bsf 
        from queue import Queue
        
        if not root:
            return 
        
        que = Queue(maxsize=0)
        que.put(root)
        res = [] 
        

        
        while not que.empty():
            n = que.qsize()
            for i in range(n):
                cur = que.get()
                if i==n-1:
                    res.append(cur.val)
                if cur.left:
                    que.put(cur.left)
                if cur.right:
                    que.put(cur.right)
        return res
        


        
        
        
