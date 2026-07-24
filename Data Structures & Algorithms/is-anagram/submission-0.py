class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        if len(s) == len(t):
            for char in s:
                anagram[char] = anagram.get(char, 0) + 1
            for char in t:
                anagram[char] = anagram.get(char, 0) - 1
            if all(v == 0 for v in anagram.values()):
                return True
            else:
                return False
        else:
            return False