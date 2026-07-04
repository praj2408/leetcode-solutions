# Last updated: 7/4/2026, 4:55:41 PM
1from collections import Counter
2class Solution:
3    def containsDuplicate(self, nums: List[int]) -> bool:
4
5        freq = Counter(nums)
6
7        for key, value in freq.items():
8            if freq[key] > 1:
9                return True
10        
11        return False
12
13
14        