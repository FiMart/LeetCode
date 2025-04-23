class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_map = {"type": 0, "color": 1, "name": 2}
        rule_index = rule_map[ruleKey]
        return sum(1 for item in items if item[rule_index] == ruleValue)