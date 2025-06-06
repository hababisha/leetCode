class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) 
        sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True) 
        return [num for num, count in sorted_freq[:k]]