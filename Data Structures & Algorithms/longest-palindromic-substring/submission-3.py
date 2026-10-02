class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0
        def extendEven(s, i):
            nonlocal resIdx, resLen
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    resIdx = l
                    resLen = r - l  + 1
                l -= 1
                r += 1
            return 

        def extendOdd(s,i):
            nonlocal resIdx, resLen
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if resLen < (r - l + 1):
                    resIdx = l
                    resLen = r - l  + 1
                l -= 1
                r += 1
            return 
        for i in range(len(s)):
            extendOdd(s,i)
            extendEven(s,i)
        return s[resIdx: resIdx + resLen]