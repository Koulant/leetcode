class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_list = []
        for i in nums:
            if i in num_list:
                return True
            num_list.append(i)
        return False
            

         