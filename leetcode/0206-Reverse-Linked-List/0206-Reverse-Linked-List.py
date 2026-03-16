# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head # curr = 1
        prev = None 
        # 1 2 3 4 5 
        while curr:
            nxt = curr.next # nxt = 2
            curr.next = prev # back arrow
            prev = curr  #  pre = 1
            curr = nxt  # curr = 2
        return prev