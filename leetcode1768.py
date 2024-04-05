import itertools


class Solution(object):
    def mergeAlternately(self, word1: str, word2: str) -> str:
        (minLen, maxWord) = (len(word1), word2) if len(word1) <= len(word2) else (len(word2), word1)
        res = ''
        for i in range(minLen):
            res += word1[i] + word2[i]
        res += maxWord[minLen:]
        return res

    def mergeAlternately_short(word1: str, word2: str) -> str:
        return ''.join(a + b for a, b in itertools.zip_longest(word1, word2, fillvalue=''))


    def mergeAlternately_short_2(word1: str, word2: str) -> str:
        res = ''
        for a, b in itertools.zip_longest(word1, word2, fillvalue=''):
            temp = a + b
            res += temp
        return res

obj = Solution()
print(obj.mergeAlternately('asds', 'asd'))