class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res += strs[i] + ';'
        return res
    def decode(self, s: str) -> List[str]:
        return s.split(";")[0:-1]
        