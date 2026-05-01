class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Store results in map of sorted_s : s
        result = defaultdict(list)

        for s in strs:
            s_sorted = "".join(sorted(s)) # sort s then join resulting list
            result[s_sorted].append(s) # assign sorted_s as key equal to list of s 
        
        # return dict values for each sorted_s key 
        return list(result.values())