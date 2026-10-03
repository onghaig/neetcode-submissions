class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def extendEven(s, i):
            nonlocal count
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return 

        def extendOdd(s,i):
            nonlocal count
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return 
        for i in range(len(s)):
            extendOdd(s,i)
            extendEven(s,i)
        return count