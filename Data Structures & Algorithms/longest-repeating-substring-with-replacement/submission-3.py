from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # counter with the number 
        # just find the max of the substring when we consider k replacements
        maxSize = 0
        charSet = set(s[i] for i in range(len(s)))
        for c in charSet:
            l = 0
            r = 1
            count = 0 
            for r in range(len(s)):
                if (s[r] == c):
                    count += 1
                while (count + k < r - l + 1):
                    if (s[l] == c):
                        count -=1
                    l+=1
                maxSize = max(r - l  + 1,maxSize)
        return maxSize 