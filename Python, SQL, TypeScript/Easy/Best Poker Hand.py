class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        cnt = Counter(ranks)
        if max(cnt.values()) >= 3:
            return "Three of a Kind"
        elif max(cnt.values()) == 2:
            return "Pair"
        else:
            return "High Card"