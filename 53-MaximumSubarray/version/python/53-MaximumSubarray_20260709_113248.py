# Last updated: 7/9/2026, 11:32:48 AM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        
4
5        current = best = nums[0]
6
7        for x in nums[1:]:
8            current = max(x, current + x)
9            best = max(best, current)
10
11        return best
12