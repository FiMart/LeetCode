class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left: List[int], right: List[int], operator: str) -> List[int]:
            result = []
            for l in left:
                for r in right:
                    if operator == '+':
                        result.append(l + r)
                    elif operator == '-':
                        result.append(l - r)
                    elif operator == '*':
                        result.append(l * r)
            return result

        if expression.isdigit():
            return [int(expression)]

        results = []
        for i, char in enumerate(expression):
            if char in "+-*":
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i + 1:])
                results.extend(compute(left_results, right_results, char))

        return results