# Last updated: 6/9/2026, 1:28:33 PM
1from collections import Counter
2class Solution:
3    def maxFrequencyElements(self, nums: List[int]) -> int:
4        
5
6        freq = Counter(nums)
7
8        max_freq = max(freq.values())
9
10        ans = 0
11        for count in freq.values():
12            if count == max_freq:
13                ans += count
14
15        return ans