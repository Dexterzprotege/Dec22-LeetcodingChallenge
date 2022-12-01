# Question: https://leetcode.com/problems/determine-if-string-halves-are-alike/

# Solution 1:
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = 0, 0
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for i in range(len(s)//2):
            if s[i] in vowels:
                a += 1
        for i in range(len(s)//2, len(s)):
            if s[i] in vowels:
                b += 1
        return a == b

# Solution 2:
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = 0, 0
        i, j = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while i < j:
            if s[i] in vowels:
                a += 1
            if s[j] in vowels:
                b += 1
            i += 1
            j -= 1
        return a == b
