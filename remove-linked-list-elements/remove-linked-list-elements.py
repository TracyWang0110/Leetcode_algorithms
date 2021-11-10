# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #任何链表都要考虑头部中间尾部
        #countinous val
        dummy = ListNode(0)
        dummy.next = head
        currNode = dummy 
        
        while currNode.next:
            if currNode.next.val == val:
                currNode.next = currNode.next.next
            #如果currnode的下一个点不为value 
            else:
                currNode = currNode.next
        return dummy.next 