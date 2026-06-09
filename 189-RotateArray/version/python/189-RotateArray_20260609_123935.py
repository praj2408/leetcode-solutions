# Last updated: 6/9/2026, 12:39:35 PM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6
7        n = len(nums)
8        k %= n
9        for _ in range(k):
10            last = nums.pop()
11            nums.insert(0, last)
12        