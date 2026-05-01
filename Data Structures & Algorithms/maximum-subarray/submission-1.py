class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute force approach
        # Try every possible subarray
        # Calculate its sum
        # Keep track of max
        # return max
        result = nums[0]
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                result = max(result, total)
        
        return result