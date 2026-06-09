# Last updated: 6/9/2026, 1:06:41 PM
1from collections import Counter
2
3class Solution:
4    def topKFrequent(self, nums, k):
5        freq = Counter(nums)
6
7        buckets = [[] for _ in range(len(nums) + 1)]
8
9        for num, count in freq.items():
10            buckets[count].append(num)
11
12        res = []
13
14        for i in range(len(nums), 0, -1):
15            for num in buckets[i]:
16                res.append(num)
17                if len(res) == k:
18                    return res