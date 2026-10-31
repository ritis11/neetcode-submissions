class Solution:
    def calPoints(self, op: List[str]) -> int:
        if not op:
            return 0
        ans = []
        for val in (op):
            if val == "+":
                ans.append(ans[-1] + ans[-2])
            elif val == "C":
                ans.pop()
            elif val == "D":
               ans.append(2*ans[-1])
            else: 
                ans.append(int(val))
        return sum(ans)
        