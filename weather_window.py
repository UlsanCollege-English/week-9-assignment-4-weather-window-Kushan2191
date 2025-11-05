"""
HW04 — Weather Window: Sliding Maximum

Implement sliding_window_max(nums, k) -> list
"""

import heapq

def sliding_window_max(nums, k):
    if not nums or k <= 0:
        return []
    if k > len(nums):
        return [max(nums)]
    
    heap = []
    result = []
    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        # Remove elements out of the current window
        while heap and heap[0][1] <= i - k:
            heapq.heappop(heap)
        # When the window is full, record the max
        if i >= k - 1:
            result.append(-heap[0][0])
    return result
