# Last updated: 6/20/2026, 12:02:51 AM
1from typing import List
2
3class Solution:
4    def sortArray(self, nums: List[int]) -> List[int]:
5        temp = [0] * len(nums)
6
7        def merge_sort(left, right):
8            if left >= right:
9                return
10
11            mid = (left + right) // 2
12
13            merge_sort(left, mid)
14            merge_sort(mid + 1, right)
15
16            i, j, k = left, mid + 1, left
17
18            while i <= mid and j <= right:
19                if nums[i] <= nums[j]:
20                    temp[k] = nums[i]
21                    i += 1
22                else:
23                    temp[k] = nums[j]
24                    j += 1
25                k += 1
26
27            while i <= mid:
28                temp[k] = nums[i]
29                i += 1
30                k += 1
31
32            while j <= right:
33                temp[k] = nums[j]
34                j += 1
35                k += 1
36
37            for idx in range(left, right + 1):
38                nums[idx] = temp[idx]
39
40        merge_sort(0, len(nums) - 1)
41        return nums