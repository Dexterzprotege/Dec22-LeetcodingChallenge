# Question: https://leetcode.com/problems/sort-characters-by-frequency/

# Solution:
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        bucket = [[] for _ in range(len(s)+1)]
        for char, freq in count.items():
            bucket[freq].append(char)
        
        ans = ""
        
        n = len(s)
        while n != 0:
            for char in bucket[n]:
                ans += char * n
            n -= 1
        return ans
