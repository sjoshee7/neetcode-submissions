class Solution:

    def encode(self, strs: List[str]) -> str:
        pieces = []
        for s in strs:
            pieces.append(str(len(s)) + "#" + s)
        return "".join(pieces)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            content = s[j + 1:j + 1 + length]
            result.append(content)
            i = j + length + 1
        return result