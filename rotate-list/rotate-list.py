# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     #计算列表的长度
    def get_length(self, head):
        length = 0
        while head:
            length = length + 1
            head = head.next
        return length
            
            
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        
        length = self.get_length(head)
        
        k=k%length
        
        #把前面的指针移动N步
        
        ahead = dummy 
        
        for i in range(k):
            ahead = ahead.next 
            
        behind = dummy 
        #同时移动两个指针
        while ahead.next:
            ahead = ahead.next 
            behind = behind.next 
            
        #重组
        ahead.next = dummy.next
        dummy.next = behind.next
        behind.next = None
        
        return dummy.next
        
        
        
        