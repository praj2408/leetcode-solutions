# Last updated: 6/9/2026, 1:00:43 PM
1from collections import Counter
2class Solution:
3    def containsDuplicate(self, nums: List[int]) -> bool:
4
5
6        count = Counter(nums)
7
8        for count in count.values():
9            if count > 1:
10                return True
11
12        return False
13        