# Last updated: 7/9/2026, 10:21:14 AM
1from collections import Counter
2class Solution:
3    def majorityElement(self, nums: List[int]) -> int:
4        
5
6        candidate = 0
7        count = 0
8
9        for num in nums:
10
11            if count == 0:
12                candidate = num
13
14            if num == candidate:
15                count += 1
16            else:
17                count -= 1
18        
19        return candidate