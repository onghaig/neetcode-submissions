class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        stable = [0] * 26
        ttable = [0] * 26
        for i in range(len(s)):
            stable[ord(s[i]) % 26] += 1
            ttable[ord(t[i]) % 26] += 1
        return stable == ttable