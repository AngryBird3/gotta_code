'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
Hide Company Tags LinkedIn
Hide Tags Stack
Hide Similar Problems (H) Basic Calculator (H) Expression Add Operators

'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = list()
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r_operand = stack.pop()
                l_operand = stack.pop()
                #stack.append(str(eval(l_operand+t+r_operand))) --> This won't work as in division we want 0 -> 3/-4 
                if t == "+":
                    stack.append(l_operand + r_operand)
                elif t == "-":
                    stack.append(l_operand - r_operand)
                elif t == "*":
                    stack.append(l_operand * r_operand)
                else:
                    stack.append(int(float(l_operand)/r_operand))
                
        if len(stack) != 1:
            assert "Invalid revere polish notation"
        return stack.pop()
        
