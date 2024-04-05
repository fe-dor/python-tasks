class Solution:
    def makeGood(self, s: str) -> str:
        for idx in range(len(s) - 1):
            if abs(ord(s[idx]) - ord(s[idx + 1])) == 32:
                return self.makeGood(s[0:idx] + s[idx + 2:])
        return s


s = Solution()
print(s.makeGood("lEeetcoOdeEeE"))
