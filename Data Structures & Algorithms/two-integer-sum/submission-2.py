class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for idx, item in enumerate(nums):
            diff = target-item
            diff_dict_item = diff_dict.get(item, None)
            if diff_dict_item is None:
                diff_dict[diff] = idx
            else:
                return [diff_dict_item, idx]

        
        