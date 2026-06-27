class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures) #Default value
        mono_stack = [] #pair [idx, val]
        for i, temp in enumerate(temperatures):
            while mono_stack and temp > mono_stack[-1][1]:
                mono_stack_idx, mono_stack_temp = mono_stack.pop()
                result[mono_stack_idx] = i - mono_stack_idx
            mono_stack.append([i, temp])

            
        return result