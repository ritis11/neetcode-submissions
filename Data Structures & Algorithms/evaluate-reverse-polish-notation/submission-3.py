class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ele in tokens:
            if ele not in ['+', '-', '*', '/']:
                stack.append(int(ele))
                print(stack)
            else:
              ele_1 = (stack.pop())
              ele_2 = (stack.pop())
              if ele == "+":   
                  sum_ = int(ele_1+ele_2)
                  stack.append(sum_)                
              elif ele == "-":
                  sum_ = int(ele_2-ele_1)
                  stack.append(sum_)                
              elif ele == "/":
                  sum_ = int(ele_2/ele_1)
                  stack.append(sum_)
              elif ele == "*":
                  sum_ = int(ele_1*ele_2)
                  stack.append(sum_)
        return int(stack[0])

        