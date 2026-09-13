from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # Sort keys based on count[x], highest first
        sorted_keys = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
        # Slice the first k elements
        return sorted_keys[:k]