# Last updated: 6/20/2026, 12:02:31 AM
1from typing import List
2
3class Solution:
4    def sortArray(self, nums: List[int]) -> List[int]:
5        if len(nums) <= 1:
6            return nums
7
8        mid = len(nums) // 2
9
10        left = self.sortArray(nums[:mid])
11        right = self.sortArray(nums[mid:])
12
13        return self.merge(left, right)
14
15    def merge(self, left: List[int], right: List[int]) -> List[int]:
16        result = []
17        i = j = 0
18
19        while i < len(left) and j < len(right):
20            if left[i] <= right[j]:
21                result.append(left[i])
22                i += 1
23            else:
24                result.append(right[j])
25                j += 1
26
27        result.extend(left[i:])
28        result.extend(right[j:])
29
30        return result