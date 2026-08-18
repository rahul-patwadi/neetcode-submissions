from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
         
        sorted_items = sorted(freq.items(), key = lambda x:x[1],reverse = True)
        
        result = []
        for nums, count in sorted_items[:k]:
            result.append(nums)

        return result