class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Need to check if num appears more than once
        # Use a set 
        # Ceck all nums
        # Add num to set
        # If num already in set, return true
        # return false
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num) # 1

        return False 
