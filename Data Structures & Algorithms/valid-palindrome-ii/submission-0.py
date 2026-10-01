class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r, skipped):
            if l >= r:
                return True
            if s[l] == s[r]:
                return is_palindrome(l + 1, r - 1, skipped)
            # Characters don't match
            # If we haven't skipped yet, try both options
            if skipped == 0:
                return (is_palindrome(l+1, r, 1) or is_palindrome(l, r-1, 1))
            return False
    
        return is_palindrome(0, len(s) - 1, 0)