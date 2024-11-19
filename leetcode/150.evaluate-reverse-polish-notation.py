#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def evaluate(a,b,operator):
            if operator == '+':
                return a+b
            if operator == '-':
                return a-b
            if operator == '*':
                return a*b
            if operator == '/':
                return int(a / b) #python issue.. this does the trick

        def is_number(s):
            if s in ["+", "-", "*", "/"]:
                return False
            return True

        for token in tokens:
            if is_number(token):
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                ans = evaluate(a,b,token)
                stack.append(ans)

        return stack[0]
# @lc code=end

