# Last updated: 6/9/2026, 12:41:40 PM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6
7        n = len(nums)
8        k = k % n
9
10        # helper function to reverse part of array
11        def reverse(start, end):
12            while start < end:
13                nums[start], nums[end] = nums[end], nums[start]
14                start += 1
15                end -= 1
16
17        reverse(0, n - 1)
18        # Step 2
19        reverse(0, k - 1)
20        # Step 3
21        reverse(k, n - 1)
22                