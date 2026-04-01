class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s.lower() if char.isalnum())
        
        start, end = 0, len(cleaned) -1
        while start < end:
            if cleaned[start] != cleaned[end]:
                return False
            start += 1
            end -= 1
            
        return True