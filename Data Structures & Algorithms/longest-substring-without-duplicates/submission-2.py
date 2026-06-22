class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        p1 = 0
        p2 = 0
        seen = set()
        wordlen = len(s)
        while (p2 < len(s)):
            while (s[p2] in seen):
                seen.remove(s[p1])
                p1 += 1
            seen.add(s[p2])
            longest = max(longest, p2 - p1 + 1)
            p2 += 1
        return longest