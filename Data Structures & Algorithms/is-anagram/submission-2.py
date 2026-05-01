class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Iterate each string
        # Make it into a dict
        # Compare dicts at end
        s_dict = {}
        t_dict = {}

        for c in s:
            if c not in s_dict:
                s_dict[c] = 0
            s_dict[c] += 1

        for c in t:
            if c not in t_dict:
                t_dict[c] = 0
            t_dict[c] += 1
        
        if s_dict == t_dict:
            return True

        return False