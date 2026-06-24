class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result =[0] * len(temperatures)
        st = [] 
        # holds the days that still need a warmer days
        for idx, day in enumerate(temperatures):
            while(st and day > st[-1][1]):
                tempi, tempd = st.pop()
                result[tempi] = abs(tempi - idx)
            # check if the day is warmer than the top of the stack
            st.append([idx,day])
        return result