# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        current = head 
        length=0
        while current:
            length+=1
            current = current.next
        baseSize = length//k
        extra = length%k
        print(length)
        result =[]
        current = head
        for i in range(k):
            partSize = baseSize + (1 if extra > 0 else 0)
            extra-=1
            partHead = current
            prev = None
            for j in range(partSize):
                prev = current
                current = current.next
            if prev :
                prev.next = None
            result.append(partHead)
        while len(result) < k:
            result.append(None)
        return result
