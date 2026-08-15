from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        # this queue will track the 
        # the windows is t
        window = Counter()
        tcount = Counter(t)
        bestl = 0
        bestr = float("inf")
        need = len(tcount)
        have = 0
        l = 0
        for i,r in enumerate(s):
            # add on the right
            window[r] += 1
            if r in tcount and window[r] == tcount[r]:
                have += 1
            
            while have == need:
                if (i - l < bestr - bestl):
                    bestl = l
                    bestr = i
                window[s[l]] -= 1
                if (s[l] in tcount and tcount[s[l]] > window[s[l]]):
                    have -=1
                l += 1
        return s[bestl: bestr + 1] if bestr != float("inf") else ""
            

