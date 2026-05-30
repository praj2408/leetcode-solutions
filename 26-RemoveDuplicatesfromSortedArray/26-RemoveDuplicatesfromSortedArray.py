# Last updated: 5/30/2026, 3:52:29 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3
4
5        if not nums:
6            return 0
7
8        i = 0
9
10        for j in range(1, len(nums)):
11            if nums[j] != nums[i]:
12                i += 1
13                nums[i] = nums[j]
14
15        return i + 1
16
17
18        