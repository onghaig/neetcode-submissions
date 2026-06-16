class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #two pointer
        #first
        #second
        p1 = 0
        listsize = len(numbers)
        p2 = listsize - 1
        while p1 < p2:
            val = numbers[p1] + numbers[p2]
            if val == target:
                return [p1+1,p2+1]
            elif val > target:
                p2 -= 1
            else:
                p1 += 1
        return [p1,p2] 