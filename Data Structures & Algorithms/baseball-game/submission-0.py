class Solution:
    def calPoints(self, operations: List[str]) -> int:
        value = []

        for i in operations:
            if i == "+":
                value.append(value[-1] + value[-2])
            
            elif i == "C":
                value.pop()
            
            elif i == "D":
                value.append(value[-1] * 2)

            else:
                value.append(int(i))
        return sum(value)
