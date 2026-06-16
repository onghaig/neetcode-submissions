class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0
        operators = {'+', '-', '*', '/'}
        for i,e in enumerate(tokens):
            if e in operators:
                b, a = str(stack.pop()), str(stack.pop())
                exp =  a + e + b 
                # pop 1st and 2nd, then eval
                temp = eval(exp)
                stack.append(int(temp))
            else:
                stack.append(int(e))
        return  stack.pop()
