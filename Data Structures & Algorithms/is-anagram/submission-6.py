class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Need to track count of chars in s and t
        # If all counts are equal, return true
        # Otherwise return false
        s_dict = {}
        t_dict = {}

        for s_char in s:
            if s_char not in s_dict:
                s_dict[s_char] = 1
            
            s_dict[s_char] += 1
        
        for t_char in t:
            if t_char not in t_dict:
                t_dict[t_char] = 1
            
            t_dict[t_char] += 1

        if s_dict == t_dict:
            return True
        
        return False
