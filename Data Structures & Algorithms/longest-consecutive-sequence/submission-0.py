class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for num in nums_set:
            run_length = 1
            if num - 1 in nums_set:
                continue
            while num + 1 in nums_set:
                run_length += 1
                num = num + 1
            max_length = max(max_length, run_length)
        

        return max_length