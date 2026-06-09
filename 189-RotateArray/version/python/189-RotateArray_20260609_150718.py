# Last updated: 6/9/2026, 3:07:18 PM
1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6
7        n = len(nums)
8        k %= n
9
10        def rotate_array(left, right):
11            while left < right:
12                nums[right], nums[left] = nums[left], nums[right]
13                left += 1
14                right -= 1
15
16        rotate_array(0, n-1)
17        rotate_array(0, k-1)
18        rotate_array(k, n-1)
19
20        return nums