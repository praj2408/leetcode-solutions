# Last updated: 6/3/2026, 11:33:10 AM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        
4
5        mp = {}
6
7        for i, num in enumerate(numbers):
8            complement = target - num
9
10            if complement in mp:
11                return [mp[complement]+1, i+1]
12            mp[num] = i
13         