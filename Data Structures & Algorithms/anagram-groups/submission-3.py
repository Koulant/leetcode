class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use an array of size 26 to map letters to numbers
        # Count the frequency of each char in strs
        # Use the array as the key in the hash map to group strings
        result = defaultdict(list) # defaultdict creates a dict with the given callable
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1 # Use non-zero values to track char counts
            
            result[tuple(count)].append(s) # map count to a list of strings with that count
            # use append to add one ele instead of +=
            # += on a list creates a new list then reassigns

        return list(result.values())
