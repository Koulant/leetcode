class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Char by char comparison approach
        # Check each index
        # Check each char in str
        # if last index or char does not equal same index char of first str
        # return s up to index i
        # otherwise return strs[0]
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i] # Get as far as common letters go
        return strs[0]


        