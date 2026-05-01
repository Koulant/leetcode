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

        nums_map = {}

        for i, num, in enumerate(nums):
            nums_map[num] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_map and nums_map[diff] != i:
                return[i, nums_map[diff]]

        return []