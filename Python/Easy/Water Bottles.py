class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drinks = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            new_bottles = empty_bottles // numExchange
            total_drinks += new_bottles
            empty_bottles = new_bottles + (empty_bottles % numExchange)

        return total_drinks