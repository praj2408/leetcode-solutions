# Last updated: 7/9/2026, 11:32:02 AM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        
4
5        current = nums[0]
6        best = nums[0]
7
8        for i in range(1, len(nums)):
9            current = max(nums[i], current + nums[i])
10            best = max(best, current)
11
12        return best
13