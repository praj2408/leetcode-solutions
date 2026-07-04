# Last updated: 7/4/2026, 4:51:26 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3
4
5
6
7        seen = {}
8
9        for i, num in enumerate(nums):
10
11            complement = target - num
12
13            if complement in seen:
14                return [seen[complement], i]
15
16            seen[num] = i
17