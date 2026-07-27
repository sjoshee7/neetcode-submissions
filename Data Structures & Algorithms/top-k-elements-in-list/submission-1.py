class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for key, value in frequency.items():
            buckets[value].append(key)

        output = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                output.append(num)
                if len(output) == k:
                    return output
