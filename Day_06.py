# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubPath(self, head, root):
        def dfs(head  , root) :
            if not head :
                return True
            if not root :
                return False
            if head.val != root.val:
                return False
            return dfs(head.next , root.right) or dfs(head.next , root.left)
        if not head:
            return True
        if not root :
            return False
        return dfs(head , root) or self.isSubPath(head , root.left) or self.isSubPath(head , root.right)
