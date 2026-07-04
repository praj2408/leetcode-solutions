# Last updated: 7/4/2026, 5:01:40 PM
1from collections import Counter
2
3class Solution:
4    def isAnagram(self, s: str, t: str) -> bool:
5
6        return sorted(s) == sorted(t)
7        