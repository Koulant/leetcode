class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Key insight, anagrams are equal when sorted
        # Iterate strs
        # Sort each str
        # Set sorted str as key in hash map to map to list of words/str in strs
        # return hash map as a list
        group_anagrams = []
        anagram_map = {}

        for s in strs:
            s_asc = "".join(sorted(s))

            if s_asc not in anagram_map:
                anagram_map[s_asc] = []
            anagram_map[s_asc].append(s)
        
        return list(anagram_map.values())