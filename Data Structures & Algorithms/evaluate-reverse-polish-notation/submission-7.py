class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ele in tokens:
            if ele == "+":
                cal = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(cal)

            elif ele == "-":
                cal = stack[-2] - stack[-1]
                stack.pop()
                stack.pop()
                stack.append(cal)

            elif ele == "*":
                cal = stack[-1] * stack[-2]
                stack.pop()
                stack.pop()
                stack.append(cal)
            elif ele == "/":
                cal = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(cal)

            else:
                stack.append(int(ele))
            
        return stack[0]

        