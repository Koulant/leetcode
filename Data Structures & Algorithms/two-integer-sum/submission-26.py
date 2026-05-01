class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Make a hash map of nums
        nums_map = {} # map of value : index
        
        for i, n in enumerate(nums): 
            diff = target - n # other number needed
            if diff in nums_map: # have we need other number?
                return [nums_map[diff], i] # if so, return the indicies
            nums_map[n] = i # if not, add the number to the mapping
