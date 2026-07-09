# Last updated: 7/9/2026, 10:20:12 AM
1from collections import Counter
2class Solution:
3    def majorityElement(self, nums: List[int]) -> int:
4        
5
6        freq = Counter(nums)
7
8        for key, value in freq.items():
9            if value > (len(nums)//2):
10                return key