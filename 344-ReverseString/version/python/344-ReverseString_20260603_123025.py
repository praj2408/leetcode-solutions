# Last updated: 6/3/2026, 12:30:25 PM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6
7        left = 0
8        right = len(s)-1
9
10        while left < right:
11            s[left], s[right] = s[right], s[left]
12            left += 1
13            right -= 1
14
15
16        