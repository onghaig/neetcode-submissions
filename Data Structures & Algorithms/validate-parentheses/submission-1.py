class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        table = {')' : '(', ']' : '[', '}' : '{'}
        for ch in s:
            if ch in table:
                if st and st[-1] == table[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
        return True if not st else False