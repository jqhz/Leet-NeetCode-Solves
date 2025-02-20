class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        aStr = ""
        for c in s:
            if c.isalnum():
                aStr = aStr+c.lower()
        
        return aStr==aStr[::-1]