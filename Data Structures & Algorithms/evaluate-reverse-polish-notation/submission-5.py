class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        for token in tokens:
            if token == '+':
                my_stack.append(my_stack.pop() + my_stack.pop())
            elif token == '-':
                second_num = my_stack.pop()
                first_num = my_stack.pop()
                my_stack.append(first_num - second_num)
            elif token == '*':
                my_stack.append(my_stack.pop() * my_stack.pop())
            elif token == '/':
                denominator = my_stack.pop()
                numerator = my_stack.pop()
                quotient = int(float(numerator) / denominator)
                my_stack.append(quotient)
            else:
                my_stack.append(int(token))
        return my_stack[0]