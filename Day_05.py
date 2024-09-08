# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        nums_set = set(nums)  
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current and current.next:
            if current.next.val in nums_set:
                current.next = current.next.next  # Skip the node
            else:
                current = current.next  # Move to the next node
        return dummy.next
