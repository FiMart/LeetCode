class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0.0
        prev_limit = 0

        for limit, rate in brackets:
            if income > limit:
                tax += (limit - prev_limit) * rate / 100.0
                prev_limit = limit
            else:
                tax += (income - prev_limit) * rate / 100.0
                break

        return tax