class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0

        for i in range(len(s)):
            char = s[i]

            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            char_index[char] = i

            current_len = i - left + 1
            if current_len > max_len:
                max_len = current_len

        return max_len