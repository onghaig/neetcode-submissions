class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = [] 
        # will hold idx, day in the stack, and we push onto the stack every element
        # we remove in a loop until the day is no longer greater
        for i, t in enumerate(temperatures):
            while (st and t > st[-1][1]):
                ci, ct = st.pop()
                res[ci] = abs(ci - i)
            st.append([i,t])
        return res