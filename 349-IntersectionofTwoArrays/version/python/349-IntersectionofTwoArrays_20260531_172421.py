# Last updated: 5/31/2026, 5:24:21 PM
1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3
4        results = []
5
6        for i in nums1:
7
8            for j in nums2:
9                if j == i and j not in results:
10                    results.append(j)
11
12            
13        return results
14        