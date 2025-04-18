class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {" ": " "}
        i = 0
        for c in key:
            if c not in d:
                d[c] = chr(ord("a") + i)
                i += 1
        return "".join([d[c] for c in message])