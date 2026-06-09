# Last updated: 6/9/2026, 12:58:42 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3
4
5        s = set()
6
7        for num in nums:
8            s.add(num)
9
10        return len(nums) != len(s)
11        