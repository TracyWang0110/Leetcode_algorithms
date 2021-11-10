# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #check how long 
        #分奇偶讨论
        #2个指针，一个快指针，一个慢指针
        if head is None:
            return None
        slow = head
        fast = head
        #slow is one step, fast is two steps
        
        while fast and fast.next:
            #if first middle while slow.next and fast.next.next
            slow = slow.next
            fast = fast.next.next 
        return slow 