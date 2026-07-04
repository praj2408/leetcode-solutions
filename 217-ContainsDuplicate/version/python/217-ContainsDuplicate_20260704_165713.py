# Last updated: 7/4/2026, 4:57:13 PM
1from collections import Counter
2class Solution:
3    def containsDuplicate(self, nums: List[int]) -> bool:
4
5        return len(nums) != len(set(nums))
6
7
8        