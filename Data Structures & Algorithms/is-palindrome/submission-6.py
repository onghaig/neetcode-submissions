class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we have a string S, we want to know if it is a palindrome r not
        #simply create two pointers and travrse both through

        left = 0 
        right = len(s) - 1

        while left <= right:
            if s[left].isalnum() is False:
                left += 1
                continue
            if s[right].isalnum() is False:
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -=1

        return True