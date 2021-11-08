# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #"dummy" note that allow us to easily return the head of the merged list later        
        dummy = ListNode(-1)  
        prev = dummy
        while l1 and l2: #untill the at least one of l1 and l2 points to null
            if l1.val <= l2.val:
                prev.next = l1 #connect to previous to l1
                l1 = l1.next #increment of l1
                
            else:
                prev.next = l2 #do the same thing as l1
                l2 = l2.next 
            prev = prev.next  #increament of prev
        #at least one of l1 and l2 still have nodes
        if l1 is not None:
            prev.next = l1
        else:
            prev.next = l2
        
        return dummy.next