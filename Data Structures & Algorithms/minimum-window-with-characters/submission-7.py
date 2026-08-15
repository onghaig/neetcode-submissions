from collections import Counter
class Solution:
    def minWindow(self, s, t):
        countT = Counter(t)
        winCount = Counter()
        if (t == ""):
            return ""
        sl = 0
        bestl = sl
        bestr = float('inf')
        bestWindow = float('inf')
        have = 0
        need = len(countT)
        for i,r in enumerate(s):
            l = s[sl]
            winCount[r] += 1
            if have != need and countT[r] == winCount[r]:
                have += 1
            while have == need:
                l = s[sl]
                if (i - sl +1) < bestWindow:
                    bestl = sl
                    bestr = i
                    bestWindow =  i- sl + 1
                winCount[l] -= 1
                if (l in countT and winCount[l] < countT[l]):
                    have -= 1
                sl += 1
        return s[bestl:bestr+1] if bestWindow != float('inf') else ""