"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""


class Solution:
    """
        #Поиск наибольшей совпадающей части двух строк (неправильно понял условие)
        def gcdOfStrings1(self, str1: str, str2: str) -> str:
        [shorter_string, longer_str] = [str1, str2] if len(str1) < len(str2) else [str2, str1]
        if shorter_string not in longer_str:
            return ""
        for shift_value in range(1, len(shorter_string)):
            for shift_step in range(shift_value + 1):
                part_of_srt = shorter_string[shift_step:len(shorter_string) - shift_value + shift_step]
                if part_of_srt in longer_str:
                    return part_of_srt
        return ''"""

    #Посмотрел другие решения
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        [shorter_len, longer_len, shorter_str] = [len(str1), len(str2), str1] if (
                len(str1) < len(str2)) else [len(str2), len(str1), str2]

        def gcd(num1: int, num2: int):
            return num2 if num1 % num2 == 0 else gcd(num2, num1 % num2)

        return shorter_str[0:gcd(longer_len, shorter_len)]

    #Написал сам
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        [shorter_str, longer_str] = [str1, str2] if len(str1) < len(str2) else [str2, str1]
        shorter_len = len(shorter_str)
        res = ""
        for i in range(1, shorter_len + 1):
            if ((shorter_str[0:i] * (shorter_len // i) == shorter_str) &
                    (shorter_str[0:i] * (len(longer_str) // i) == longer_str)):
                res = shorter_str[0:i]
        return res


s = Solution()
print(s.gcdOfStrings("ABC", "ABCABC"))
