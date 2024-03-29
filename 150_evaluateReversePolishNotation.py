from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        current_position = 0

        while len(tokens) > 1:

            # Move the current position pointer to the next operator.
            while tokens[current_position] not in "+-*/":
                current_position += 1

            # Extract the operator and numbers from the list.
            operator = tokens[current_position]
            number_1 = int(tokens[current_position - 2])
            number_2 = int(tokens[current_position - 1])

            # Calculate the result to overwrite the operator with.
            if operator == "+":
                tokens[current_position] = number_1 + number_2
            elif operator == "-":
                tokens[current_position] = number_1 - number_2
            elif operator == "*":
                tokens[current_position] = number_1 * number_2
            else:
                tokens[current_position] = int(number_1 / number_2)

            # Remove the numbers and move the pointer to the position
            # after the new number we just added.
            tokens.pop(current_position - 2)
            tokens.pop(current_position - 2)
            current_position -= 1

        return tokens[0]

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]

    def evalRPNN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]

tokens = ["2","1","+","3","*"]
so = Solution()
print(so.evalRPNN(tokens))

"""
150. Evaluate Reverse Polish Notation
Medium

3826

686

Add to List

Share
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.



Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
Accepted
490,171
Submissions
1,116,646
"""