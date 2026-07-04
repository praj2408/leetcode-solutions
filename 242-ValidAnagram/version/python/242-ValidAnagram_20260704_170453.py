# Last updated: 7/4/2026, 5:04:53 PM
1from collections import Counter
2
3class Solution:
4    def isAnagram(self, s: str, t: str) -> bool:
5
6
7        if len(s) != len(t):
8            return False
9
10        count = Counter(s)
11
12        for ch in t:
13            if ch not in count:
14                return False
15            count[ch] -= 1
16
17            if count[ch] < 0:
18                return False
19
20        return True
21        