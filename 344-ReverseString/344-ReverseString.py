# Last updated: 2/23/2026, 5:40:06 PM
1class Solution:
2    def reverseString(self, s: List[str]) -> None:
3        """
4        Do not return anything, modify s in-place instead.
5        """
6        left = 0
7        right = len(s) - 1
8
9        while left < right:
10            s[left], s[right] = s[right], s[left]
11            left += 1
12            right -= 1
13        