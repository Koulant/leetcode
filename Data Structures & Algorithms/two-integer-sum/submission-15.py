class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # output = []

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             output = [i, j]
        #             return output

        # Optimized approach
        # Enumerate the list, value : index
        # Check each k:v
        # if diff = target - value
        # if diff in indicies and not same index
        # return indicies
        # otherwise return empty list

        # Cleanest
        nums_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_map:
                return [nums_map[diff], i]
            nums_map[num] = i
