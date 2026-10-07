from collections import Counter
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        curpos = 0
        remaining = len(s)
        for r in range(len(s)):
            while curpos < len(t):
                print(s[r], t[curpos], remaining)
                if t[curpos] == s[r]:
                    remaining -= 1
                    curpos += 1
                    break
                curpos += 1
        return remaining == 0 