class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        new = sorted(s);
        new2 = sorted(t);
        return new == new2;