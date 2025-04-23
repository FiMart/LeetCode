class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort(reverse=True)
        ans = 0
        while amount[0] > 0:
            amount[0] -= 1
            amount[1] -= 1
            ans += 1
            amount.sort(reverse=True)
        return ans