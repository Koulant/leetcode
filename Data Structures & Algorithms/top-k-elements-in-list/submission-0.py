class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}

        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1

        sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

        result = []
        for num, count in sorted_items[:k]:
            result.append(num)

        return result

        