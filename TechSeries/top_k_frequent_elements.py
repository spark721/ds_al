
# LeetCode 347

# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# Note:
#     You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
#     Your algorithm's time complexity must be better than O(n log n), 
#       where n is the array's size.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while len(heap) > 0:
            res.append(heapq.heappop(heap)[1])
        return res

# O(n) for building Hashmap
# O(n*log(k)) Time Heap pushes
# Space O(k) - Heap
# Space O(n) - Hashmap

# Space - O(n)
# Time - O(n*log(k))
