class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        stable = [0] * 256
        ttable = [0] * 256
        for i in range(len(s)):
            stable[ord(s[i])] += 1
            ttable[ord(t[i])] += 1
        return stable == ttable