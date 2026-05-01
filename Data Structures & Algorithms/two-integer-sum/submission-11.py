class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output = []

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             output = [i, j]
        #             return output

        # Optimized approach
        # Enumerate the list, mapping index: value
        # Check each value, once
        # If difference = target - nums[i] in hash map, return index/key
        nums_map = {}
        for i in range(len(nums)):
            number = nums[i]
            diff = target - number
            if diff in nums_map:
                return [nums_map[diff], i]
            nums_map[nums[i]] = i
