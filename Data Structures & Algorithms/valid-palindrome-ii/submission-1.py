class Solution:
    def validPalindrome(self, s: str) -> bool:
        k = 1
        def is_palindrome(l, r, deletions_left):
            # Base case: pointers have crossed or met
            if l >= r:
                return True
            
            # Characters match, move inward
            if s[l] == s[r]:
                return is_palindrome(l + 1, r - 1, deletions_left)
            
            # Characters don't match
            # If we still have deletions available, try both options
            if deletions_left > 0:
                return (is_palindrome(l + 1, r, deletions_left - 1) or 
                        is_palindrome(l, r - 1, deletions_left - 1))
            
            # No deletions left
            return False
        
        return is_palindrome(0, len(s) - 1, k)