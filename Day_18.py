class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        dummy = ListNode(0)
        currentDummy = dummy
        current = head
        while current :
            currentValue = current.val
            if currentValue not in arr:
                currentDummy.next = ListNode(currentValue)
                currentDummy = currentDummy.next
            arr.append(currentValue)
            current = current.next
        return dummy.next
