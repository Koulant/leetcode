class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = ""
        for char in s:
            if char.isalnum():
                valid_chars += char.lower()
        return valid_chars == valid_chars[::-1]
                