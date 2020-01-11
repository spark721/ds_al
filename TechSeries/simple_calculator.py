
class Solution:
    def __eval_helper(self, expression, index):
        op = '+'
        result = 0
        while index < len(expression):
            char = expression[index]
            if char in ('+', '-'):
                op = char
            else:
                value = 0
                if char.isdigit():
                    value = int(char)
                elif char == '(':
                    (value, index) = self.__eval_helper(expression, index + 1)
                if op == '+':
                    result += value
                if op == '-':
                    result -= value
            index += 1
        return (result, index)

    def eval(self, expression):
        return self.__eval_helper(expression, 0)[0]


exp1 = '- (3 + ( 2 - 1))'
exp2 = '3 + 2 + 7 - 8'
exp3 = '(1 + (2 + (3 + (4 + 5))))'
print(Solution().eval(exp1))
print(Solution().eval(exp2))
print(Solution().eval(exp3))
