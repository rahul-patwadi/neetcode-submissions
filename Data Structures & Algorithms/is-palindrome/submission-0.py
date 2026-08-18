class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s1 = ''.join(char for char in s if char.isalnum())
        s2 = s1.lower()
        s3 = s2[::-1]
        print(s2)
        if s2 == s3:
            return True
        return False

