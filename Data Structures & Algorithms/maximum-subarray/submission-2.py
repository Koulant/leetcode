class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Optimal approach using dynamic programming
        # if running sum reduces current, drop it and start from current element
        current = 0
        result = nums[0]

        for i in range(len(nums)):
            if current < 0:
                current = 0 # drop the bad prefix
            current += nums[i]
            result = max(result, current)
        
        return result
