class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")
        left = left.replace("-", "+-")
        right = right.replace("-", "+-")
        left = left.split("+")
        right = right.split("+")
        left = [x for x in left if x]
        right = [x for x in right if x]
        a, b = 0, 0
        for x in left:
            if "x" in x:
                if len(x) == 1:
                    a += 1
                elif len(x) == 2 and x[0] == "-":
                    a -= 1
                else:
                    a += int(x[:-1])
            else:
                b -= int(x)
        for x in right:
            if "x" in x:
                if len(x) == 1:
                    a -= 1
                elif len(x) == 2 and x[0] == "-":
                    a += 1
                else:
                    a -= int(x[:-1])
            else:
                b += int(x)
        if a == 0 and b == 0:
            return "Infinite solutions"
        elif a == 0 and b != 0:
            return "No solution"
        else:
            return f"x={b // a}"