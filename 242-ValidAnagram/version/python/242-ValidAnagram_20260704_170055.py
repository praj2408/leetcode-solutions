# Last updated: 7/4/2026, 5:00:55 PM
1from collections import Counter
2
3class Solution:
4    def isAnagram(self, s: str, t: str) -> bool:
5
6
7        return Counter(s) == Counter(t)
8        