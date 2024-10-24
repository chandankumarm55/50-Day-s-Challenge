class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # If the string is already a palindrome, return 1
        if s == s[::-1]:
            return 1
        # If it's not a palindrome, we can remove it in 2 steps
        return 2
