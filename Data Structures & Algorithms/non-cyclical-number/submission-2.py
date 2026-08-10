from math import pow
class Solution:
    def isHappy(self, n: int) -> bool:
        # positive integer, replace it with the sume of the squares of its digits
        # repeat until the number equals 1 
        # if it does not reach 1, it is cyclical
        num = str(n)
        seen = set()
        while (True):
            total = 0
            for digit in range(len(num)):
                cur = pow(int(num[digit]),2)
                total += cur
            if(total == 1):
                break
            if (total in seen):
                return False
            seen.add(total)
            num = str(math.ceil(total))
        return True
            