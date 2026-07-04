# Last updated: 7/4/2026, 10:58:06 PM
1from collections import Counter
2
3class Solution:
4    def isAnagram(self, s: str, t: str) -> bool:
5
6        if len(s) != len(t):
7            return False
8        
9        count = Counter(s)
10
11        for ch in t:
12            if ch not in count:
13                return False
14            count[ch] -= 1
15
16            if count[ch] < 0:
17                return False
18            
19        return True