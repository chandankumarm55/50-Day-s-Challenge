# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            currentElement = current
            nextElement = current.next
            currentgcd = gcd(currentElement.val , nextElement.val)
            gcdNode = ListNode(currentgcd)
            current.next = gcdNode
            gcdNode.next = nextElement
            current = current.next.next
        return head
