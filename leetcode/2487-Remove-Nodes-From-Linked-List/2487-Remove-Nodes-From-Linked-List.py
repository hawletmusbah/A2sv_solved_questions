# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Step 1: Reverse the linked list
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        head = reverse(head)
        
        # Step 2: Traverse and remove nodes smaller than the max seen so far
        curr = head
        max_val = head.val
        
        while curr and curr.next:
            if curr.next.val < max_val:
                # Skip the next node (delete it)
                curr.next = curr.next.next
            else:
                # Update max_val and move forward
                max_val = curr.next.val
                curr = curr.next
                
        # Step 3: Reverse back to original order
        return reverse(head)