class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1 = 0
        p2 = len(s) - 1
        def swap(s,x,y):
            temp = s[x]
            s[x] = s[y]
            s[y] = temp
        while p1 < p2:
            swap(s, p1,p2)
            p1 += 1
            p2 -= 1
        