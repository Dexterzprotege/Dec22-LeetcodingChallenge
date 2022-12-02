# Question: https://leetcode.com/problems/determine-if-two-strings-are-close/

# Solution:
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1, w2 = [0] * 26, [0] * 26
        s1, s2 = set(), set()
        
        for c in word1:
            w1[ord(c)-ord('a')] += 1
            s1.add(c)
        
        for c in word2:
            w2[ord(c) - ord('a')] += 1
            s2.add(c)
        
        return sorted(w1) == sorted(w2) and s1 == s2
