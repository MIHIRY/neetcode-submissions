class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        value = []

        for i in tokens:
            if i == "+":
                a = value.pop()
                b = value.pop()
                value.append(b+a)
            
            elif i == "*":
                a = value.pop()
                b = value.pop()
                value.append(b*a)
            
            elif i == "-":
                a = value.pop()
                b = value.pop()
                value.append(b-a)
            
            elif i == "/":
                a = value.pop()
                b = value.pop()
                value.append(int(b/a))
            else:
                value.append(int(i))

        return value[-1]