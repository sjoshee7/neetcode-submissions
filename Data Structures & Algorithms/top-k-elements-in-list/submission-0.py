import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        
        for num in nums:
            frequency[num] = frequency.get(num, 0) - 1

        pairs = []

        for key, value in frequency.items():
            pairs.append((value, key))

        heapq.heapify(pairs)

        output = []
        
        for i in range(k):
            output.append(heapq.heappop(pairs)[1])

        return output