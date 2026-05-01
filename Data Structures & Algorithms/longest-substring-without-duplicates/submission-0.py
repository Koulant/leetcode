class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Find the longest length of continuous chars withuot a repeating char
        # Iterate s
        # store chars in hash map of char : count
        # If map has key greater than 2, store max and continue
        # return max at the end
        l = 0
        result = 0
        char_set = set()
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            result = max(result, r - l + 1)
            
        return result
