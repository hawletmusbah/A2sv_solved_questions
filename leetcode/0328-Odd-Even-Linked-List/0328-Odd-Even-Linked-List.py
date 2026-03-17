# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return head
        elif  not head.next:
            return head
        # 1 2 3 4 5

        odd = head 
        even = even_head = head.next
       
        while even and even.next:
            odd.next = even.next 
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
            
           
        return head