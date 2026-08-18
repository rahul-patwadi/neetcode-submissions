class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s1 = ''.join(char for char in s if char.isalnum())
        s1 = s1.lower()
        s2 = s1[::-1]
        return s1 == s2

